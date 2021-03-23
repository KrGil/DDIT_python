import matplotlib as mpl
import numpy as np                #  뭔가 많이 import 시켰다. 그냥 그른가부다 하고 넘어가자.
import matplotlib.pyplot as plt   #  여러분이 코딩을 할땐 그냥 복붙하여 사용하면 된다.

# import 어쩌고 as 저쩌고 라는 코드는 from 어쩌고 import 와 비슷하다. 다만 코드를 칠때마다 "저쩌고.어쩌고 안의 기능"이라고 해야 코드가 작동한다.
# 바로 아래코드도 보면 mpl.rcParams[~~~] 이라고 써있다. rcParams 를 바로 쓰지 않는다.
import pymongo


def getPrices(s_name):    
    connection = pymongo.MongoClient("mongodb://localhost")
    db = connection.python
    
    stock = db.stock
    rows = stock.find({"s_name" : s_name})
    
    first_price = rows[0]['s_price']
    print("첫가격 : ",first_price)

    price = []
    for r in rows :
        price_rate= int(r['s_price'])/ int(first_price)
        price.append(price_rate)
        print(price)
    
    return price

    
mpl.rcParams['legend.fontsize'] = 10            # 그냥 오른쪽 위에 뜨는 글자크기 설정이다.

fig = plt.figure()                                # 이건 꼭 입력해야한다.
ax = fig.gca(projection='3d')

zs = []

# DB에서 값 가져와서 넣기
zs.append(getPrices("삼성전자"))
zs.append(getPrices("LG"))
zs.append(getPrices("SK"))

x = np.zeros(len(zs[0])) #종류
y = range(len(zs[0])) #시간 고정

ax.plot(x+0, y, zs[0], label='samsung')        # 위에서 정의한 x,y,z 가지고 그래프그린거다.
ax.plot(x+1, y, zs[1], label='lg')        # 위에서 정의한 x,y,z 가지고 그래프그린거다.
ax.plot(x+2, y, zs[2], label='sk')        # 위에서 정의한 x,y,z 가지고 그래프그린거다.
ax.legend()                                        # 오른쪽 위에 나오는 글자 코드다. 이거 없애면 글자 사라진다. 없애도 좋다.

plt.show()