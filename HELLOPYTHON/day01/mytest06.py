# 가위바위보를 만드시오.
import random

me = input("가위바위보 중 하나를 입력하세요")
me_num = 0;
com = random.randrange(0, 3)
result = ""
res = 1

if me == "가위":
    me_num = 0
elif me == "바위":
    me_num = 1
elif me == "보":
    me_num = 2
else :
    res = 0

if res == 1:
    print("me = "+str(me_num))
    print("com = " + str(com))
    if me_num == com :
        result = "비겼다"
    elif (me_num == 0 and com == 1) or (me_num == 1 and com == 2) or (me_num == 2 and com == 0):
        result = "졌다"
    else :
        result = "이겼다"
    
    # 컴퓨텨 숫자 => 가위바위보
    if com == 0:
        com = "가위"
    elif com== 1:
        com = "바위"
    elif com == 2:
        com = "보"
    
    print("나 : ", me)
    print("컴 : ", com)
    print("결과 : ", result)
else :
    print("가위바위보 모르냐")
    