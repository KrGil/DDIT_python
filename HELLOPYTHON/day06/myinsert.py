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

sql = "INSERT INTO sample (col01, col02, col03) VALUES (%s, %s, %s)"
cnt = cursor.execute(sql,('6','6','4'))
gil_db.commit()
gil_db.close()
print("cnt", cnt)

