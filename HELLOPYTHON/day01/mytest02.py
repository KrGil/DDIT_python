# 2~10까지의 2의 배수 합
# (1+n)*n / 2

sum = 0
for i in range(2, 11):
    if(i % 2 == 0):
        print(i)
        sum += i
        
print("2~10까지의 2의 배수의 합: ", sum)     
