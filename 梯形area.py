#輸入float x1,x2
#求f(x)=x^3在x1~x2區間內的梯形面積
# area = (x2-x1)*(x2^3+x1^3)/2
x1,x2 = map(float,input().split())
print((x2-x1)*(x2**3+x1**3)/2)