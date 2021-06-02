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
import pickle
import os.path

ignored_exceptions = (NoSuchElementException,StaleElementReferenceException)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
list_of_manufacturers = ['AMD', 'Intel', 'Asrock', 'ASUS', 'GIGABYTE',
                         'Inno3D', 'KFA2', 'MSI', 'Palit', 'PNY', 'PowerColor'
                         'Sapphire', 'Zotac', 'A-Data', 'AMD Radeon', 'Apacer',
                         'Corsair', 'Crucial', 'Crucial Ballistix', 'Dell',
                         'G.Skill', 'Goodram', 'HP', 'Hynix', 'HyperX', 'JRam',
                         'Kingston', 'Lenovo', 'Micron', 'Neo Forza', 
                         'Patriot Memory', 'QUMO', 'Samsung', 'Silicon Power',
                         'Team Group', 'Thermaltake', 'Transcend']

class DnsShopParser(object):
    def forward_parse(self, number_pgs, req, _class_prod):
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
                WebDriverWait(driver, 0, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='pagination-widget__page-link pagination-widget__page-link_next ']"))).click()
            except Exception as ex:
                print(ex)
        driver.quit()
        self.save_data(list_name, list_price, list_link, "1", _class_prod)
        #print("1: \n", len(list_price), "### ", number_pgs)

    def back_parse(self, number_pgs, req, _class_prod):
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
                for item in title_prod_list[::-1]:
                    list_name.append(item.text) 
                
                link_prod_list = driver.find_elements(By.XPATH, "//a[@class='catalog-product__name ui-link ui-link_black']")
                for item in link_prod_list[::-1]:
                    list_link.append(item.get_attribute("href"))
                
                price_prod_list = driver.find_elements(By.XPATH, "//div[@class='product-buy__price']")
                for item in price_prod_list[::-1]:
                    list_price.append(item.text)

                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
                WebDriverWait(driver, 0, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='pagination-widget__page-link pagination-widget__page-link_prev ']"))).click()
            except Exception as ex:
                print(ex)
        driver.quit()
        self.save_data(list_name, list_price, list_link, "2", _class_prod)
        #print("2: \n", list_price)

    def get_url(self, driver):
        return driver.current_url

    def get_count_pages(self, req):
        driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
        driver.maximize_window()
        driver.get(req)
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2.5)
            WebDriverWait(driver, 0, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='pagination-widget__page-link pagination-widget__page-link_last ']"))).click()
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

    
    def save_data(self, name_prod_list, price_list, link_prod_list, num:str, _class_prod):
        d = self._conversion_to_(name_prod_list, price_list, link_prod_list)
        dir = os.path.abspath(os.curdir)
        with open(dir[:-6] + 'data/' + 'data' + num + _class_prod + '.picle', 'wb') as f:
            pickle.dump(d, f)


    def avg_price(self, d:list, min_border:int, max_border:int, text:str):
        index_list = list()
        for i in range(len(d)):
            if d[i].get("Цена товара") >= min_border and d[i].get("Цена товара") <= max_border and (text in d[i].get("Название товара")):
                index_list.append(i)
            elif d[i].get("Цена товара") >= min_border and d[i].get("Цена товара") <= max_border and (text in 'All'):
                index_list.append(i)  
            else:
                continue     
        return index_list  

    def most_manufactures(self, d:list, index_list:list):
        temp = list()
        for i in range(len(index_list)):
            for j in range(len(list_of_manufacturers)):
                if list_of_manufacturers[j] in d[i].get("Название товара"):
                    temp.append(list_of_manufacturers[j])

        result = list()
        for i in range(len(list_of_manufacturers)):
            result.append(
                {
                    list_of_manufacturers[i]:temp.count(list_of_manufacturers[i])
                }
            )          
        return result    
    
    def indexing_list(self, some_list:list):
        temp = list()
        for i in range(len(some_list)):
            temp.append(i)
        return temp    

    def get_symb_of_str(self, text:str):
        temp = list()
        try:
            for i in text:
                if not i.isdigit():
                    temp.append(i)
        except TypeError:
            temp.append('All') 
        return ''.join(temp).replace(' ', '')

   
