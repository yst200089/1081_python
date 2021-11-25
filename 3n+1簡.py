def countDigital(n):
    count = 0
    if n ==1 :
        return 1
    while n != 1 :
        if n % 2 == 0 :
            n = n / 2
            count += 1
        else:
            n = n * 3 + 1
            count += 1
    return count
def main():
    i=int(input())
    print(i,countDigital(i))
if __name__ == '__main__' :
    main()