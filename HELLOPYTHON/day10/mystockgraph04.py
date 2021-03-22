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
from day10.myselect import getAllPrices, getCnt

if __name__ == '__main__':
    mpl.rcParams['legend.fontsize'] = 10            # 그냥 오른쪽 위에 뜨는 글자크기 설정이다.

    fig = plt.figure()                                # 이건 꼭 입력해야한다.
    ax = fig.gca(projection='3d')
    
    zs = []
    zs = getAllPrices()    
    x = np.zeros(len(zs[0])) #종류
    y = range(len(zs[0])) #시간 고정
    
    # DB에서 값 가져와서 넣기
    
    for i in range(len(zs)):
        ax.plot(x+i, y, zs[i])
    # ax.plot(x+0, y, zs[0], label='s000020')        # 위에서 정의한 x,y,z 가지고 그래프그린거다.
    ax.legend()                                        # 오른쪽 위에 나오는 글자 코드다. 이거 없애면 글자 사라진다. 없애도 좋다.
    
    plt.show()


