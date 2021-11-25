 # A------B
#      C-----D
#判斷線段AB和線段CD是否重疊？
# -> 看C(起點)是否位於線段AB之間
#判斷線段AB和線段CD的終點？
# -> 若D介於線段AB之間，則終點為B，反之，則為D
def main():
    #有n條線段
    n = int(input())
    data = list()
    for i in range(n):
        #將所有線段的開始和結束端點加到data
        data.append(list(map(int,input().split())))
    data.sort()
    #將第一條線段作為基準
    left, right, total= data[0][0], data[0][1], 0
    for s in data :
        #查看每個線段的開始端點，如果小於上一條線的結束端點，代表線段重疊
        if s[0]<= right :
            #判斷上一條和這一條線的結束端點大小
            right = s[1] if s[1] > right else right
        else :
            #若沒有重疊就結算一次長度，再算下一條線
            total, left, right = total+right-left, s[0], s[1]
    total += right-left
    print(total)
if __name__ == '__main__' :
    main()