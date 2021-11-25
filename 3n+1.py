#學號：108213052
#姓名：楊心慈
def countDigital(n):
    count = 1
    if n == 1 : #如果 n = 1 結束
        return 1
    while n > 1: #如果n是偶數，那麼 n=n/2
        if n % 2 == 0 :
            n = n / 2
            count += 1
        else : #否則，n=3*n+1
            n= 3 * n + 1
            count += 1
    return count
#比較 countDigital(n)的長度大小，找最大值
def maxDigital(i,j):
    max=0
    for x in range (i,j):
        length = countDigital(x)
        if length > max :
            max = length
    #測完每一個數，max就是答案
    return max
def main():
    i,j= map(int,input().split())
    #確認i,j的大小
    if i < j:
        max = maxDigital(i,j)
        print(i,j,max)
    if i > j:
        i,j= j,i
        max = maxDigital(i,j)
        print(j,i,max)
if __name__ == '__main__' :
    main()
#最後修改：2019年9月23日15:41