import numpy as np

a = np.zeros((10, 10), dtype=int) #덧셈과 뺄셈의 항등원

print(a)
print(a.shape)

b = np.reshape(a,(20,5))

print(b)
