import requests
from bs4 import BeautifulSoup
import datetime
import pymysql
import time
import sys
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
        temp = []
        s_name = info.dt.text 
        s_price = info.dd.span.text
        s_price = s_price.replace(",", "")
        s_code_text = info.dd['id']
        s_code = s_code_text[len(s_code_text)-6:len(s_code_text)]
        # print()
        cnt = insert(s_code, s_name, s_price, nowDatetime)
    time.sleep(60)

# yyyymmdd:HHMM 24시간표시
# %Y-%m-%d %H:%M
# for item in items:
    # temp = []
    # name = item.select_one(".tbody > dt > a")["title"]
    # price = item.select_one(".tbody dd span:first-child")
    # price_1 = price.text
    # code = item.select_one(".tbody dd")["id"]
    # code_1 = code[code.rindex("_")+1:]
    # temp.append(name)
    # temp.append(price_1)
    # temp.append(code_1)
    #
    # c_list.append(temp)
    #
# with open('c_list.csv', "w", encoding="utf-8", newline="") as f:
    # writer = csv.writer(f)
    # writer.writerow(["주식이름", "가격", "코드"])
    # writer.writerow(c_list)
# f.close
#
# f = open('c_list.csv', 'r', encoding="utf-8", newline="" )
# rdr = csv.reader(f)
# for line in rdr:
    # print(line)
# f.close