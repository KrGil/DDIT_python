# 불러오기

import pandas as pd
import pymysql

gil_db = pymysql.connect(
    user='root', 
    passwd='python', 
    host='127.0.0.1', 
    db='python', 
    charset='utf8'
)
cursor = gil_db.cursor(pymysql.cursors.DictCursor)

#* 쓰는걸 지양하자. 파이썬 ;이 있거나 없거나 상관이 없다.
sql = "SELECT col01, col02, col03 FROM sample;"
cursor.execute(sql)
result = cursor.fetchall()

result = pd.DataFrame(result)
print(result)
gil_db.close()


