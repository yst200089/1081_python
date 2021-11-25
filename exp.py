#求ax＾2 + bx + c = 0的解
#輸入三個float,代表上面方程式的係數
a,b,c=map(float, input().split())
print((-b+(b*b-4*a*c)**0.5)/(2*a),(-b-(b*b-4*a*c)**0.5)/(2*a))