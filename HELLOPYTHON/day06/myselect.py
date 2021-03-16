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

sql = "SELECT * FROM sample;"
cursor.execute(sql)
result = cursor.fetchall()

result = pd.DataFrame(result)

print(result)



