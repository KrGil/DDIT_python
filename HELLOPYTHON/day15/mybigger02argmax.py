import numpy as np
a = [0,0,4,0,0,
     0,0,0,0,0]
a_n = np.array(a)

# 배열의 가장 큰 값을 불러오는 매서드
pred = np.argmax(a_n)

print(pred)