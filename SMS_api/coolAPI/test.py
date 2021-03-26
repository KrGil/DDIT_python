import random
random.randrange(1,25)

s1 = '01024504831'
s2 = '01062054021'
s3 = '01043082280'
s4 = '01097192470'
s5  ='01023389130'
s6  ='01044551277'
s7  ='01072291828'
s8  ='01028764096'
s9  ='01068287610'
s10 ='01098326711'
s11 ='01054589526'
s12 ='01039350724'
s13 ='01051310924'
s14 ='01063600660'
s15 ='01046260081'
s16 ='01090482372'
s17 ='01028750267'
s18 ='01051140124'
s19 ='01085544580'
s20 ='01036918419'
s21 ='01046867852'
s22 ='01020159875'
s23= '01039211655'
s24 ='01034407800'
s25 ='01051537035'


list = []

list.append(s1)
list.append(s2)
list.append(s3)
list.append(s4)
list.append(s5)
list.append(s6)
list.append(s7)
list.append(s8)
list.append(s9)
list.append(s10)
list.append(s11)
list.append(s12)
list.append(s13)
list.append(s14)
list.append(s15)
list.append(s16)
list.append(s17)
list.append(s18)
list.append(s19)
list.append(s20)
list.append(s21)
list.append(s22)
list.append(s23)
list.append(s24)
list.append(s25)

print(list)
print(set(list))

cnt = 0
list_ran = ""
for i in set(list) :
    if cnt == 0:
        list_ran += i
    if cnt !=1 :
        list_ran += ","+i
    if cnt ==1 :
        break
    cnt += 1
print(list_ran)



