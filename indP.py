def main():
    n=int(input())
    data=list(map(int,input().split()))
    minPass,maxFail=101,-1
    for score in data:
        if minPass >= 60 and minPass < score :
            minPass = score
        if maxFail < 60 and maxFail < score :
            maxFail = score
    data.sotr()
    if minPass = 101 :
        minPass = 'worst case'
    if maxFail = -1 :
        maxFail = 'best case'
    print(maxFail,minPass)