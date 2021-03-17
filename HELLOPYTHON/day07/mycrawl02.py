import requests
from bs4 import BeautifulSoup
from _csv import writer
import csv
from scipy.spatial.transform import _rotation_spline
 
response = requests.get('https://www.sedaily.com/Stock/Quote/?mobile')
 
txt = response.text
 
# print(txt)

soup = BeautifulSoup(txt, 'html.parser')
# items = soup.select(".tbody")
# print(items)
c_list = []

for info in soup.select(".tbody"):
    
    s_name = info.dt.text 
    s_price = info.dd.span.text
    s_code_text = info.dd['id']
    s_code = s_code_text[len(s_code_text)-6:len(s_code_text)]
    
    print(s_name, end="\t")
    print(s_price, end="\t")
    print(s_code)

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