import time
import csv
import pandas as pd
import xlsxwriter
import json
import pickle

def upload_to_json_file(d:list, name_ctg:str):
    with open(name_ctg + "_data.json", "w", encoding="utf-8") as file:
        json.dump(d, file, indent=12, ensure_ascii=False)

def upload_to_csv_file(d:list, name_ctg:str):
        try:
            with open(name_ctg + "_data.csv", mode="w") as w_file:
                names = ['Название товара', 'Цена товара', 'Ссылка на товар']
                file_writer = csv.DictWriter(w_file, delimiter = ",", lineterminator="\r", fieldnames=names)
                file_writer.writeheader()
                file_writer.writerows(d)
        except Exception:
            return 'create csv file failed'

def upload_to_xlsx_file(d:list, name_ctg:str):
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

def open_data(path:str):
        with open(path, 'rb') as f:
            d = pickle.load(f)
        return d