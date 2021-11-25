# define a function to check if n is a prime
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
    x = int(input())
    if (isPrime(x)) :
        print('prime')
    else :
        print('Non prime')
if __name__ == '__main__' :
    main()