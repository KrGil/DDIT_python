# matploblib
import pandas as pd
import pymysql
from sympy.physics.quantum.circuitplot import matplotlib
from networkx.generators import line

gil_db = pymysql.connect(
    user='root', 
    passwd='python', 
    host='127.0.0.1', 
    db='python', 
    charset='utf8'
)
cursor = gil_db.cursor()

#* 쓰는걸 지양하자. 파이썬 ;이 있거나 없거나 상관이 없다.
sql = "SELECT  s_price FROM stock where s_code = '000020'"
cursor.execute(sql)
result = cursor.fetchall()
print(result)
# result = pd.DataFrame(result)
gil_db.close()
gil_db = pymysql.connect(
    user='root', 
    passwd='python', 
    host='127.0.0.1', 
    db='python', 
    charset='utf8'
)
cursor = gil_db.cursor()
sql = "SELECT s_price FROM stock where s_code = '000040'"
cursor.execute(sql)
result2 = cursor.fetchall()
gil_db.close()


import matplotlib as mpl
import matplotlib.pyplot as plt
matplotlib.lines

value = result
plt.figure(figsize = (10,4))

plt.plot(result[:], lw = 1.5, label = "1")
plt.plot(result2[:], lw = 1.5, label = "2")

plt.grid(True)
plt.legend(loc=0) 

plt.xlabel('time')
plt.ylabel('money')

plt.title("1")
plt.show()
