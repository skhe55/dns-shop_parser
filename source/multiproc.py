from multiprocessing import Process
import time
import os.path
import pickle

sd = ['Alison', 'AMasn', 'Geny']
def avg_price(d, max, min):
    index_list = list()
    for i in range(len(d)):
        if d[i].get("Price") >= min and d[i].get("Price") <= max:
            index_list.append(i)
    return index_list        

def most_manf(d, idx):
    temp = list()
    for i in range(len(idx)):
        for j in range(len(sd)):
            if sd[j] in d[i].get("Name"):
                temp.append(sd[j])
    return temp

if __name__ == '__main__':
    d = [
        {
            "Name":"Alison sd56546",
            "Price": 4535,
            "Link": "asdasd::"
        },
        {
            "Name":"AMasn sdsdsd",
            "Price": 1000,
            "Link": "sdsddd::"
        },
        {
            "Name":"Geny 435 34",
            "Price": 3000,
            "Link": "dfdf::"
        },
        {
            "Name":"Alison xXXXXXX546",
            "Price": 4225,
            "Link": "asdasd::"
        }
    ]
    idx = avg_price(d, 5000, 500)
    temp = most_manf(d, idx)
    print(idx)
    print(temp.count('Alison'))
