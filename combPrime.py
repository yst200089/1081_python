#學號：108213052
#姓名：楊心慈
def isPrime(n):
    # num由 2 開始
    num = 2
    # 1不是質數
    if n <= 1 :
        return False
    # 直到num 到 n-1
    while num < n :
        #若可以整除
        if n % num == 0 :
            #就不是質數
            return False
        #測試下一個數字
        num = num + 1
    #都不能整除，就是質數
    return True
def findPrime(prime, n, result):
    # 如果數字加起來等於 n ,輸出
    if n <= 0 :
        if n == 0 :
            print(*result)
        return
    # 將每個質數排列
    for i in range(len(prime)):
        findPrime(prime[i+1:], n-prime[i], result+[prime[i]])
def main():
    #輸入一個整數
    n = int(input())
    prime=[]
    for num in range(2,n+1) :
        if isPrime(num) :
            prime.append(num)
    # 如果是質數
    if isPrime(n):
        # 直接輸出質數本身
        print(n)
    #如果不是質數
    else :
        #就輸出質數相加等於n的組合
        findPrime(prime, n, [])
if __name__ == '__main__' :
    main()
#最後修改：2019年11月01日09:05