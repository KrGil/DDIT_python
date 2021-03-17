import requests
from bs4 import BeautifulSoup
import datetime
import pymysql

response = requests.get('https://www.sedaily.com/Stock/Quote/?mobile')
 
txt = response.text
 
# print(txt)

soup = BeautifulSoup(txt, 'html.parser')
c_list = []
now = datetime.datetime.now()
nowDatetime = now.strftime('%Y%m%d:%H%M')

gil_db = pymysql.connect(
    user='root', 
    passwd='python', 
    host='127.0.0.1', 
    db='python', 
    charset='utf8'
)
cursor = gil_db.cursor(pymysql.cursors.DictCursor)

sql = "INSERT INTO stock (s_code, s_name, s_price, in_date) VALUES (%s, %s, %s, %s)"


for info in soup.select(".tbody"):
    temp = []
    s_name = info.dt.text 
    s_price = info.dd.span.text
    s_price = s_price.replace(",", "")
    s_code_text = info.dd['id']
    s_code = s_code_text[len(s_code_text)-6:len(s_code_text)]

    cursor.execute(sql,(s_code, s_name, s_price, nowDatetime))
    print(s_name, end="\t")
    print(s_price, end="\t")
    print(s_code)
gil_db.commit()
gil_db.close()
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