import requests
from bs4 import BeautifulSoup
import datetime
import time
import pymongo


def insertStock(s_code, s_name, s_price, nowDatetime):
    connection = pymongo.MongoClient("mongodb://localhost")
    db = connection.python
    stock = db.stock
    
    doc = {'s_name': s_name, 's_price': s_price,'s_price':s_price, "in_date" : nowDatetime}
    stock.insert_one(doc)
    
    
if __name__ == '__main__':
    insertStock("1", "1", "1")