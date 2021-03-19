import numpy as np                #  뭔가 많이 import 시켰다. 그냥 그른가부다 하고 넘어가자.

# import 어쩌고 as 저쩌고 라는 코드는 from 어쩌고 import 와 비슷하다. 다만 코드를 칠때마다 "저쩌고.어쩌고 안의 기능"이라고 해야 코드가 작동한다.
# 바로 아래코드도 보면 mpl.rcParams[~~~] 이라고 써있다. rcParams 를 바로 쓰지 않는다.
import pymysql
import time

def getPrices():    
    gil_db = pymysql.connect(
        user='root', 
        passwd='python', 
        host='127.0.0.1', 
        db='_stock_old', 
        charset='utf8'
    )
    cursor = gil_db.cursor()
    
    sql_col = """
                SELECT COLUMN_NAME
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_SCHEMA = '_stock_old' AND TABLE_NAME = 'stock_sync_0121'
                    AND column_NAME != 'in_time';
              """
    cursor.execute(sql_col)
    rows_col = cursor.fetchall()
    
    columns = []
    rows_arr = np.array(rows_col)
    # columns에 컬럼 담아주기
    for item in rows_arr :
        columns.append(item[0])
     
    select_col =", ".join(columns[:10])
    count_col = len(columns[:10])
    print("컬럼명들 : ",select_col)
    print("컬럼갯수 : ",count_col )
    # 총 갯수 구하기
    sql_total = f"""
            SELECT count({count_col})
            FROM stock_sync_0121
            """
    cursor.execute(sql_total)
    total = cursor.fetchall()
    count = total[0][0] # 총 데이터(열) 갯수
    print("총 열 갯수 : ", count)
    
    ## 실제 데이터 구하기
    sql_prices = f"""
            SELECT {select_col}
            FROM stock_sync_0121;
            """
    print(sql_prices)
    cursor.execute(sql_prices)
    prices = cursor.fetchall()
    ## 시작가
    first_price =np.array(prices[0])
    print("시작가 : ", first_price)

    ## result에 결과값들 하나씩 담아주기.
    result = []
    result.append(select_col) ## column이름들.
    result.append(count) ## 총 데이터 갯수
    print("컬럼명 : ", result[0])
    print("총 열 갯수 : ", result[1])
    print(type(count))
    print(type(count_col))
    ## a[0] = 3892
    ## a[1] = 3892
    # current_price = 0
    # price = []
    # print(len(select_col))
    
    a = []
    b = []
    for i in range(count_col) :
        for j in range(count) :
            print(prices[j][i])
            b.append(prices[j][i])
        a.append(b)
     
        
    gil_db.close()
    return 0

if __name__ == '__main__':
    getPrices()