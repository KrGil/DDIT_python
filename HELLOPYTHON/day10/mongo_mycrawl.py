import requests
from bs4 import BeautifulSoup
import datetime
import time
import pymongo


def insert(s_code, s_name, s_price, nowDatetime):
    connection = pymongo.MongoClient("mongodb://localhost")
    db = connection.python
    stock = db.stock
    
    doc = {'s_name': s_name, 's_price': s_price,'s_price':s_price, "in_date" : nowDatetime}
    stock.insert_one(doc)
    

cnd = 0
# while True :
for i in range(10) :
    cnd+= 1;
    print(cnd)
    response = requests.get('https://www.sedaily.com/Stock/Quote/?mobile')
    txt = response.text
    soup = BeautifulSoup(txt, 'html.parser')
    nowDatetime = datetime.datetime.now().strftime('%Y%m%d:%H%M') # 입력할 때 날짜가 다를 수 있어서 python으로 한다.
  
    for info in soup.select(".tbody"):
        s_name = info.dt.text 
        s_price = info.dd.span.text
        s_price = s_price.replace(",", "")
        s_code_text = info.dd['id']
        s_code = s_code_text[len(s_code_text)-6:len(s_code_text)]
        
        cnt = insert(s_code, s_name, s_price, nowDatetime)
        
    time.sleep(60)
