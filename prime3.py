#學號：108213052
#姓名：楊心慈
def isPrime(n):
    #difinition of prime : 2~n-1 都不能整除n
    #how to write a while loop from 2 to n-1
    num = 2 #num由 2 開始
    while num < n : # 直到num 到 n-1
        if n % num == 0 : #若可以整除
            return False #就不是質數
        num = num + 1 #測試下一個數字
    return True #都不能整除，就是質數
def main() :
    n = int(input())
    for num in range(2,n+1):
        if isPrime(num) : #判斷n是不是質數
            print(num) #如果n是，列上去
if __name__ == '__main__' :
    main()
#最後修改：2019年9月25日23:05