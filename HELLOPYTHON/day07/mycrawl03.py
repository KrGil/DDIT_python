import requests
from bs4 import BeautifulSoup
import datetime
import pymysql
import time

gil_db = pymysql.connect(
    user='root', 
    passwd='python', 
    host='127.0.0.1', 
    db='python', 
    charset='utf8'
)
cursor = gil_db.cursor(pymysql.cursors.DictCursor)

def insert_sql():
    sql = """
        INSERT INTO stock (
            s_code, s_name, s_price, in_date
        ) VALUES (
            %s, %s, %s, %s
        )"""
    return sql

def update_sql():
    sql = """
        UPDATE stock SET (
        s_code = %s, s_name = %s, s_price = %s, in_date = %s
        )"""
    return sql

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
    
        cnt = cursor.execute(insert_sql(),(s_code, s_name, s_price, nowDatetime))
        
    gil_db.commit()
    time.sleep(60)

gil_db.close()
