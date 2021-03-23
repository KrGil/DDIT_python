import matplotlib as mpl
import numpy as np                #  뭔가 많이 import 시켰다. 그냥 그른가부다 하고 넘어가자.
import matplotlib.pyplot as plt   #  여러분이 코딩을 할땐 그냥 복붙하여 사용하면 된다.
import pymongo


def getPrices(s_name):    
    arr=[]
    connection = pymongo.MongoClient("mongodb://localhost")
    db = connection.python
    stock = db.stock
    
    rows = stock.find({"s_name" : s_name}).sort("in_date", 1)
    
    first_price = rows[0]['s_price']
    print("첫가격 : ",first_price)

    for r in rows :
        int_s_price = int(r['s_price'])/int(first_price)
        arr.append(int_s_price)
    return arr

if __name__ == '__main__':
    arr = getPrices("삼성전자")
    print(arr)
