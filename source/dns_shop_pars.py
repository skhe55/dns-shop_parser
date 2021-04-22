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
    def __init__(self, driver, req, ignored_exceptions):
        self.driver = driver
        self.req = req
        self.ignored_exceptions = ignored_exceptions

    def parse(self):
        self.driver.maximize_window()
        self.driver.get(self.req)
        list_name = list()
        list_price = list()
        list_link = list()
        while True:
            try:
                time.sleep(5)
                title_prod_list = self.driver.find_elements(By.XPATH, "//a[@class='catalog-product__name ui-link ui-link_black']/span[1]")
                for item in title_prod_list:
                    list_name.append(item.text) 

                link_prod_list = self.driver.find_elements(By.XPATH, "//a[@class='catalog-product__name ui-link ui-link_black']")
                for item in link_prod_list:
                    list_link.append(item.get_attribute("href"))

                price_prod_list = self.driver.find_elements(By.XPATH, "//div[@class='product-buy__price']")
                for item in price_prod_list:
                    list_price.append(item.text)
   
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
                WebDriverWait(self.driver, 5, ignored_exceptions=self.ignored_exceptions).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='pagination-widget__page-link pagination-widget__page-link_next ']"))).click()
                
            except Exception as ex:
                print(ex)
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
    
    def makeHyperLink(self, text:str, link:str):
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

   
