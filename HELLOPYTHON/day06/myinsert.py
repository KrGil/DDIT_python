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

sql = "INSERT INTO sample (col01, col02, col03) VALUES ('3', 3, '3');"
cursor.execute(sql)
gil_db.commit()
