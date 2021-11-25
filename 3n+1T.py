#給n，找出n的序列長度
def seqLen(n):
    Len = 1
    #3n+1序列是以找到1當終止
    while n != 1 :
        if n % 2 == 0 :#even then n/2
            n = n // 2
        else :#odd ,then 3n+1
            n = 3 * n + 1
        len = len + 1
    return len
#給begin,end找出其中3n+1序列最長的
def findSol(begin,end):
    #但題目說，不一定begin會比end小，所以要檢查一下
    if begin > end:
        begin,end= end,begin
    max = 0 #紀錄目前找到最長的是多少
    #逐一檢查(begin,end)之間每一個序列的長度
    for n in range (begin,end+1) :
        len = seqLen(n)
        if len > max:
            max = len
    #測完每一個數，max就是答案
    return max
def main() :
    # read in spect
    begin,end = map(int,input().split())
    #find solution
    #then print result
    print(begin,end,findSol(begin,end))
if __name__ == '__main__' :
    main()