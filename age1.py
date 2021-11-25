#已知今年是2019
#input birth year
# age =2019-birth year
#0 ~ 20 : 少年
#21 ~ 40 : 青年
#41 ~ 60 : 中年
# > 60 : 老年
#    print child
age = 2019 - int(input())
if age <=20 :
    print('少年')
elif age <= 40 :
    print('青年')
elif age <= 60 :
    print('中年')
else : 
    print('老年') 