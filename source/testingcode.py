from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from multiprocessing import Process, Pipe 
import pickle
start_time = time.time()
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

class Parsing(object):
    def __init__(self, ignored_exceptions):
        self.ignored_exceptions = ignored_exceptions

    def get_url(self, driver):
        return driver.current_url

    def get_count_pages(self, req):
        driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
        driver.maximize_window()
        driver.get(req)
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2.4)
            WebDriverWait(driver, 0, ignored_exceptions=self.ignored_exceptions).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='pagination-widget__page-link pagination-widget__page-link_last ']"))).click()
            url = self.get_url(driver)
        except Exception as ex:
            print(ex)
        finally:
            driver.quit()    
        return url

    def _conversion_to_(self, name_prod_list, price_list, link_prod_list):
        temp_list = list()
        d = list()
        for s in price_list:
            temp = s.replace(' ', '')
            temp = temp.replace('₽', '')
            temp = temp.replace('\n', '/')
            temp_list.append(temp)
            temp = ''

        price_list.clear()

        for item in temp_list:
            try:
                price_list.append(int(item))
            except ValueError:
                price_list.append(int(item[:item.find('/')]))

        for i in range(len(name_prod_list)):
            d.append({
                "Название товара": name_prod_list[i],
                "Цена товара": price_list[i],
                "Ссылка на товар": link_prod_list[i]
            }) 
        return d 

    def save_data(self, name_prod_list, price_list, link_prod_list, num:str):
        d = self._conversion_to_(name_prod_list, price_list, link_prod_list)
        with open('data' + num + '.picle', 'wb') as f:
            pickle.dump(d, f)

    def open_data(self, path:str):
        with open(path, 'rb') as f:
            d = pickle.load(f)
        return d

    def forward_parse(self, number_pgs, req):
        number_pgs = number_pgs / 2
        if type(number_pgs) == float:
            number_pgs = round(number_pgs) + 1
        driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
        driver.maximize_window()
        driver.get(req)
        list_name = list()
        list_price = list()
        list_link = list()
        for i in range(number_pgs):
            try:
                time.sleep(5)
                title_prod_list = driver.find_elements(By.XPATH, "//a[@class='catalog-product__name ui-link ui-link_black']/span[1]")
                for item in title_prod_list:
                    list_name.append(item.text) 

                link_prod_list = driver.find_elements(By.XPATH, "//a[@class='catalog-product__name ui-link ui-link_black']")
                for item in link_prod_list:
                    list_link.append(item.get_attribute("href"))

                price_prod_list = driver.find_elements(By.XPATH, "//div[@class='product-buy__price']")
                for item in price_prod_list:
                    list_price.append(item.text)
   
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
                WebDriverWait(driver, 0, ignored_exceptions=self.ignored_exceptions).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='pagination-widget__page-link pagination-widget__page-link_next ']"))).click()
            except Exception as ex:
                print(ex)
                #break
        driver.quit()
        self.save_data(list_name, list_price, list_link, "1")
        print("1: \n", len(list_price), "### ", number_pgs)

    def back_parse(self, number_pgs, req):
        number_pgs = number_pgs / 2
        if type(number_pgs) == float:
            number_pgs = round(number_pgs)
        driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
        driver.maximize_window()
        driver.get(req)
        list_name = list()
        list_price = list()
        list_link = list()
        for i in range(number_pgs):
            try:
                time.sleep(5)
                title_prod_list = driver.find_elements(By.XPATH, "//a[@class='catalog-product__name ui-link ui-link_black']/span[1]")
                for item in title_prod_list:
                    list_name.append(item.text) 

                link_prod_list = driver.find_elements(By.XPATH, "//a[@class='catalog-product__name ui-link ui-link_black']")
                for item in link_prod_list:
                    list_link.append(item.get_attribute("href"))

                price_prod_list = driver.find_elements(By.XPATH, "//div[@class='product-buy__price']")
                for item in price_prod_list:
                    list_price.append(item.text)
   
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
                WebDriverWait(driver, 0, ignored_exceptions=self.ignored_exceptions).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='pagination-widget__page-link pagination-widget__page-link_prev ']"))).click()
            except Exception as ex:
                print(ex)
                #break
        driver.quit()        
        self.save_data(list_name, list_price, list_link, "2")
        print("2: \n", len(list_price))

# 25.004719257354736 seconds #
# 5 pages -  59.72163772583008 seconds #
# 5 pages - 50.0101 seconds #
# 9 pages - 1.10 minutes #
# 47 pages - 4.04 minutes #
if __name__ == "__main__":
    ignored_exceptions = (NoSuchElementException,StaleElementReferenceException)
    list_get_requests = [        
            "https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/", 
            "https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/",
            "https://www.dns-shop.ru/catalog/17a89a3916404e77/operativnaya-pamyat-dimm/"
        ]
    pars = Parsing(ignored_exceptions)
    url = pars.get_count_pages(list_get_requests[0])
    page = url[-2:].replace('=', '')
    process_1 = Process(target=pars.forward_parse, args=(int(page), list_get_requests[0],)) 
    process_1.start()
    process_2 = Process(target=pars.back_parse, args=(int(page), url,))
    process_2.start()
    # p = Parsing(ignored_exceptions)
    # d = p.open_data('data1.picle')
    # d1 = p.open_data('data2.picle')
    # print(d)
    # print(d1)
    print(" %s seconds " % (time.time() - start_time))


