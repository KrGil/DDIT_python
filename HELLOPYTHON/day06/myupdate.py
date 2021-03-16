# 불러오기
import pymysql
import pandas as pd

gil_db = pymysql.connect(
    user='root', 
    passwd='python', 
    host='127.0.0.1', 
    db='python', 
    charset='utf8'
)
cursor = gil_db.cursor(pymysql.cursors.DictCursor)

sql = "UPDATE sample SET col01 = 3, col03 = 3 WHERE col01 = 1;"
        
cursor.execute(sql)
gil_db.commit()
