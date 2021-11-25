def main():
    n = int(input())
    data = list(map(int,input().split()))
    data.sort()
    maxFail, minPass = 'best case', 'worst case'
    for v in data :
        if v < 60 :
            maxFail = v
            continue
        if v >= 60 :
            minPass = v
            break
    print(maxFail, minPass)
if __name__ == '__main__' :
    main()