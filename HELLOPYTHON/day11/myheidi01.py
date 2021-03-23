# 불러오기
import pymysql
import pandas as pd
import numpy as np

def getList(s_name):    
        
    gil_db = pymysql.connect(
        user='root', 
        passwd='python', 
        host='127.0.0.1', 
        db='python', 
        charset='utf8'
    )
    cursor = gil_db.cursor()
    
    #* 쓰는걸 지양하자. 파이썬 ;이 있거나 없거나 상관이 없다.
    sql = f"""
            SELECT s_code, s_name, s_price, in_date 
            FROM stock
            WHERE s_name = '{s_name}'
            """
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(rows[2][2])
    
    # price = []
    list = []
    for row in rows:
        # price.append(row[2])
        list.append(row)
    
    gil_db.close()
    return list

if __name__ == '__main__':
    arr = getList("LG")
    arr = np.array(arr)
    print(arr)

