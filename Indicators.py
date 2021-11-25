#學號：108213052
#姓名：楊心慈
def main():
    #輸入學生總人數
    n = int(input())
    #輸入每個學生的分數
    scores = list(map(int,input().split()))
    #將分數由小到大依序排序
    scores.sort()
    #輸出分數
    print(scores[0],end = '')
    for v in range(1,n+1):
        print(' ' + str(scores[v]),end = '')
    print()
    min = 101
    max = -1
    for i in scores :
        #在及格分數裏找出最接近60的數
        if i < min and i >= 60 :
            min = i
        #在不及格分數裏找出最接近60的數
        if i > max and i < 60 :
            max = i
    #如果全數及格時，輸出 best case
    if max == -1 :
        print('best case')
    #如果沒有，輸出最高不及格分數
    else :
        print(max)
    #如果全數不及格時，輸出 worst case 
    if min == 101 :
        print('worst case')
    #如果沒有，輸出最低及格分數
    else :
        print(min)
if __name__ == '__main__' :
    main()
#最後修改：2019年10月15日20:42