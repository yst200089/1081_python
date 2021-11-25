#sum(n)的定義
#if n <= 1 then n
# otherwise n + sum(n-1)
def sum(n):
    if n <= 1:
        return n 
    return n + sum(n-1)
def main():
    n = int(input())
    print(sum(n))
if __name__ == '__main__' :
    main()