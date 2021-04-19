from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import pandas as pd
import xlsxwriter

class DnsShopParser(object):
    def __init__(self, driver, req):
        self.driver = driver
        self.req = req

    def parse(self):
        driver.maximize_window()
        driver.get(self.req)
        list_name = list()
        list_price = list()
        list_link = list()
        while True:
            next_page_btn = driver.find_elements(By.XPATH, "//a[@class='pagination-widget__page-link pagination-widget__page-link_next ']")

            time.sleep(14)
            title_prod_list = driver.find_elements(By.XPATH, "//a[@class='catalog-product__name ui-link ui-link_black']/span[1]")
            for item in title_prod_list:
                list_name.append(item.text) 

            link_prod_list = driver.find_elements(By.XPATH, "//a[@class='catalog-product__name ui-link ui-link_black']")
            for item in link_prod_list:
                list_link.append(item.get_attribute("href"))

            price_prod_list = driver.find_elements(By.XPATH, "//div[@class='product-buy__price']")
            for item in price_prod_list:
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
            temp = temp.replace('\n', '/')
            temp_list.append(temp)
            temp = ''

        price_list.clear()

        for item in temp_list:
            try:
                price_list.append(int(item))
            except ValueError:
                price_list.append(int(item[:item.find('/')]))

        for i in range(len(price_list)):
            if price_list[i] >= minimum_border and price_list[i] <= maximum_border:
                result_list.append(price_list[i])
                index_list.append(i)
            else:
                continue

        return index_list    
    
    def makeHyperLink(text:str, link:str):
        return '=HYPERLINK("%s", "%s")'%(link, text)

    def print_average_price_prod(self, price_list:list, name_prod_list:list, link_prod_list:list, index_list:list):
        d = list()

        for i in range(len(name_prod_list)):
            if i in index_list:
                d.append({
                    "Название товара": name_prod_list[i],
                    "Цена товара": price_list[i],
                    "Ссылка на товар": link_prod_list[i]
                })
            else:
                continue

        return d 

    def print_all_prod(self, price_list:list, name_prod_list:list, link_prod_list:list):
        d = list()

        for i in range(len(name_prod_list)):
            d.append({
                "Название товара": name_prod_list[i],
                "Цена товара": price_list[i],
                "Ссылка на товар": link_prod_list[i]
            })           

        return d

    def upload_to_csv_file(self, d:list, name_ctg:str):
        try:
            with open(name_ctg + "_data.csv", mode="w") as w_file:
                names = ['Название товара', 'Цена товара', 'Ссылка на товар']
                file_writer = csv.DictWriter(w_file, delimiter = ",", lineterminator="\r", fieldnames=names)
                file_writer.writeheader()
                file_writer.writerows(d)
        except Exception:
            return 'create csv file failed'

    def upload_to_xlsx_file(self, d:list, name_ctg:str):
        name_product = list()
        price_product = list()
        links_product = list()

        for i in range(len(d)):
            name_product.append(d[i].get('Название товара'))
            price_product.append(d[i].get('Цена товара'))
            links_product.append(d[i].get('Ссылка на товар'))

        df = pd.DataFrame()
        
        df['Название товара'] = name_product
        df['Цена товара'] = price_product
        df['Ссылка на товар'] = links_product

        writer = pd.ExcelWriter(name_ctg + '_data.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Page1', index=False)

        writer.sheets['Page1'].set_column('A:A', 120)
        writer.sheets['Page1'].set_column('B:B', 30)
        writer.sheets['Page1'].set_column('C:C', 110)
        writer.save()




if __name__ == "__main__":
    list_get_requests = ["https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/", "https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/"]
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    ignored_exceptions = (NoSuchElementException,StaleElementReferenceException)
    driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
    dns_pars = DnsShopParser(driver, list_get_requests[0])
    price, name, link = dns_pars.parse()
    index = dns_pars.average_price_pool(price, 3099, 5000)
    d = dns_pars.print_average_price_prod(price, name, link, index)
    dns_pars.upload_to_xlsx_file(d, "Videocard")
   
