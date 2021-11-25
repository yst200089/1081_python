#define a function countPrime(begin, end)
#return number of prime between(include) begin end
def isPrime(n):
    #difinition of prime : 2~n-1 都不能整除n
    if n == 1 :
        return False
    if n != 2 and n % 2 == 0 : #even is not prime
        return False
    num = 3 # num 由 3 開始
    while num * num <= n : #測試到n**0.5就好
        if n % num == 0 :
            return False 
        num = num + 2 #測試下一個奇數
    return True  #都不能整除，就是質數
def countPrime(begin, end) :
    count = 0
    num = begin
    while num <= end :
        if isPrime(num) :
            count += 1
        num += 1
    return count
def main() :
    #input 2 integer in a line
    begin, end = map(int,input().split())
    #print out number of prime between these 2 integers
    print(countPrime(begin, end))
if __name__ == '__main__' :
    main()