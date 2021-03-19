import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np                #  뭔가 많이 import 시켰다. 그냥 그른가부다 하고 넘어가자.
import matplotlib.pyplot as plt   #  여러분이 코딩을 할땐 그냥 복붙하여 사용하면 된다.

# import 어쩌고 as 저쩌고 라는 코드는 from 어쩌고 import 와 비슷하다. 다만 코드를 칠때마다 "저쩌고.어쩌고 안의 기능"이라고 해야 코드가 작동한다.
# 바로 아래코드도 보면 mpl.rcParams[~~~] 이라고 써있다. rcParams 를 바로 쓰지 않는다.

import pymysql
import pandas as pd
import numpy as np
from gevent.testing.util import getname
from astropy.table import row

def getName():
    gil_db = pymysql.connect(
        user='root', 
        passwd='python', 
        host='127.0.0.1', 
        db='python', 
        charset='utf8'
    )
    cursor = gil_db.cursor()
    
    #* 쓰는걸 지양하자. 파이썬 ;이 있거나 없거나 상관이 없다.
    sql = """
            SELECT distinct s_name
            FROM stock
            """
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    row_arr = np.array(rows)
               
    print(row_arr)
    gil_db.close()
    return row_arr

def getPrices(s_name):    
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
    
    price = []
    
    tmp = rows[0][2]
    row_int = 0
    for row in rows:
        row_int = int(row[2])
        row_result = row_int / tmp
        price.append(row_result)
    
    gil_db.close()
    return price
    
mpl.rcParams['legend.fontsize'] = 10            # 그냥 오른쪽 위에 뜨는 글자크기 설정이다.

fig = plt.figure()                                # 이건 꼭 입력해야한다.
ax = fig.gca(projection='3d')

zs = []
x = np.zeros(10) #종류
y = range(10) #시간 고정

getName()
# DB에서 값 가져와서 넣기
zname = getName()
print(zname)
    
zs.append(getPrices("LG"))
zs.append(getPrices("삼성전자"))
zs.append(getPrices("SK"))

ax.plot(x+0, y, zs[0], label='samsung')        # 위에서 정의한 x,y,z 가지고 그래프그린거다.
ax.plot(x+1, y, zs[1], label='lg')        # 위에서 정의한 x,y,z 가지고 그래프그린거다.
ax.plot(x+2, y, zs[2], label='sk')        # 위에서 정의한 x,y,z 가지고 그래프그린거다.
ax.legend()                                        # 오른쪽 위에 나오는 글자 코드다. 이거 없애면 글자 사라진다. 없애도 좋다.

plt.show()