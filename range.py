def genPrimes(n):
    #yield all primes < n
    for i in range(2,n+1):
        if isPrime(i):
            yield i
def isPrime(n):
    s = 2
    while s * s < n :
        if n % s == 0 :
            return False
        s += 1
    return True
def main():
    for x in genPrimes(int(input())):
        print(x)
if __name__ == '__main__' :
    main()