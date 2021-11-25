def main():
    n = int(input())
    data = list(map(int,input().split()))
    minPass, maxFail = 101, -1
    for score in data :
        if score >= 60 and minPass > score :
            minPass = score
        if score < 60 and maxFail < score :
            maxFail = score
    data.sort()
    print(*data)
    if minPass == 101 :
        minPass = 'worst case'
    if maxFail == -1 :
        maxFail = 'best case'
    print(maxFail,minPass)
if __name__ == '__main__' :
    main()