from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DnsShopProc_Parser(object):
    def __init__(self, driver):
        self.driver = driver

    def parse(self):
        driver.maximize_window()
        driver.get("https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/")
        list_name = []
        list_price = []
        list_link = []
        while True:
            next_page_btn = driver.find_elements(By.XPATH, "//a[@class='pagination-widget__page-link pagination-widget__page-link_next ']")

            time.sleep(14)
            title_proc_list = driver.find_elements(By.XPATH, "//a[@class='catalog-product__name ui-link ui-link_black']/span[1]")
            for item in title_proc_list:
                list_name.append(item.text)

            link_proc_list = driver.find_elements(By.XPATH, "//a[@class='catalog-product__name ui-link ui-link_black']")
            for item in link_proc_list:
                list_link.append(item.get_attribute("href"))

            price_proc_list = driver.find_elements(By.XPATH, "//div[@class='product-buy__price']")
            for item in price_proc_list:
                list_price.append(item.text)
                
            try:
                WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='pagination-widget__page-link pagination-widget__page-link_next ']"))).click() 
            except Exception:
                break

        return list_price, list_name, list_link    
         

    def average_price_pool(self, price_list:list, minimum_border:int, maximum_border:int):
        temp_list = list()
        result_list = list()
        index_list = list()
        for s in price_list:
            temp = s.replace(' ', '')
            temp = temp.replace('₽', '')
            temp_list.append(temp)
            temp = ''

        price_list = [int(item) for item in temp_list]
        for i in range(len(price_list)):
            if price_list[i] >= minimum_border and price_list[i] <= maximum_border:
                result_list.append(price_list[i])
                index_list.append(i)
            else:
                continue

        return index_list    

    def print_average_price_proc(self, price_list:list, name_proc_list:list, link_proc_list:list, index_list:list):
        d = list()

        for i in range(len(name_proc_list)):
            if i in index_list:
                d.append({
                    "Название процессора": name_proc_list[i],
                    "Цена процессора": price_list[i],
                    "Ссылка на процессор": link_proc_list[i]
                })
            else:
                continue

        return d 

    def print_all_proc(self, price_list:list, name_proc_list:list, link_proc_list:list):
        d = list()

        for i in range(len(name_proc_list)):
            d.append({
                "Название процессора": name_proc_list[i],
                "Цена процессора": price_list[i],
                "Ссылка на процессор": link_proc_list[i]
            })           

        return d
            

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    ignored_exceptions = (NoSuchElementException,StaleElementReferenceException)
    driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
    dns_pars = DnsShopProc_Parser(driver)
    price, name, link = dns_pars.parse()
    index = dns_pars.average_price_pool(price, 1399, 3550)
    print(dns_pars.print_average_price_proc(price, name, link, index))
   
