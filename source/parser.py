import requests
from bs4 import BeautifulSoup
import json
import sys
import random


class Parser:
    def __init__(self):
        self.user_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
        ]

    def asos_type_parsing(self, url:str):
        user_agent = random.choice(self.user_list)
        headers = {'User-Agent': user_agent}
        list_titles = []
        list_price = []
        list_link = []
        list_img = []
        product_data_list = []
        for it in range(1, 32):
            response = requests.get(url + f"&page={it}", headers=headers)
            src = response.text
            soup = BeautifulSoup(src, 'lxml')
            
            try:
                titles = soup.find_all(class_="_3J74XsK")
            except Exception:
                titles = "Title not found!"    
            try:
                price = soup.find_all(class_="_16nzq18")
            except Exception:
                price = "Price not found!"
            try:        
                link_product = soup.find_all(class_="_3TqU78D")
            except Exception:
                link_product = "Link on product not found!"    

            for item in titles:
                item_text = item.text
                list_titles.append(item_text)

            for item in price:
                item_text = item.text
                list_price.append(item_text) 

            for item in link_product:
                item_link = item.get("href")
                list_link.append(item_link) 

  
        for i in range(len(list_titles)):
            product_data_list.append( 
                {
                    "Имя товара": list_titles[i], 
                    "Цена товара": list_price[i],
                    "Ссылка на товар": list_link[i]
                }
            )   
        return product_data_list         

    def dns_type_parsing(self, url:str):
        user_agent = random.choice(self.user_list)
        headers = {'User-Agent': user_agent}
        categories = []
        response = requests.get(url, headers=headers)
        src = response.text
        soup = BeautifulSoup(src, 'lxml')
        

        