# 불러오기
import pymysql

def getAllPrices():    
    zs = []
    gil_db = pymysql.connect(
        user='root', 
        passwd='python', 
        host='127.0.0.1', 
        db='_stock_old', 
        charset='utf8'
    )
    cursor = gil_db.cursor()
    
    #* 쓰는걸 지양하자. 파이썬 ;이 있거나 없거나 상관이 없다.
    sql = f"""
            SELECT * FROM stock_sync_0121

            """
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    cnt10 = len(rows)
    cnt3 = len(rows[0])-1
    
    for i3 in range(cnt3):
        line = []
        first_price = rows[0][i3]
        for j10 in range(cnt10):
            if first_price ==0:
                line.append(0.9)
            else :
                line.append(rows[j10][i3]/first_price)
        zs.append(line)
    zs
    gil_db.close()
    return zs

def getCnt():
    zs = []
    gil_db = pymysql.connect(
        user='root', 
        passwd='python', 
        host='127.0.0.1', 
        db='_stock_old', 
        charset='utf8'
    )
    cursor = gil_db.cursor()
    
    #* 쓰는걸 지양하자. 파이썬 ;이 있거나 없거나 상관이 없다.
    sql = """
                SELECT COUNT(*) FROM stock_sync_0121
               """
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(rows[0][0])
    
    gil_db.close()
    return rows[0][0]
if __name__ == '__main__':
    arr = getAllPrices()
    print(arr)
    cnt = getCnt()
    print(cnt)
    pass
