import time
import csv
import pandas as pd
import xlsxwriter
import json
import pickle
import sqlite3

def upload_to_json_file(d:list):
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(d, file, indent=12, ensure_ascii=False)

def upload_to_csv_file(d:list):
        try:
            with open("data.csv", mode="w", encoding='utf-8') as w_file:
                names = ['Название товара', 'Цена товара', 'Ссылка на товар']
                file_writer = csv.DictWriter(w_file, delimiter = ",", lineterminator="\r", fieldnames=names)
                file_writer.writeheader()
                file_writer.writerows(d)
        except Exception:
            return 'create csv file failed'

def upload_to_xlsx_file(d:list):
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

    writer = pd.ExcelWriter('data.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Page1', index=False)

    writer.sheets['Page1'].set_column('A:A', 120)
    writer.sheets['Page1'].set_column('B:B', 30)
    writer.sheets['Page1'].set_column('C:C', 110)
    writer.save()

def upload_to_db_file(d:list, i):
    try:
        t_data = []
        conn  = sqlite3.connect('data.db')
        cursor = conn.cursor()
        print("Connection succ")
        cursor.execute("""CREATE TABLE IF NOT EXISTS product(name TEXT, price TEXT, link TEXT)""")
        sql_insert_with_param = """INSERT INTO product
                                (name, price, link)
                                VALUES (?, ?, ?);"""
        data_tuple = (d[i].get("Название товара"), d[i].get("Цена товара"), d[i].get("Ссылка на товар")) 
        cursor.execute(sql_insert_with_param, data_tuple) 
        conn.commit()
        print("Insert succ")  
    except sqlite3.Error as err:
        print("ERR", err)
    finally:
        if conn:
            conn.close()
            print("Connection closed")

def open_data(path:str):
        with open(path, 'rb') as f:
            d = pickle.load(f)
        return d