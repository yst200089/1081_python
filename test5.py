def main():
    n = int(input())
    m = list(map(int,input().split()))
    for r in range(max(m)+2):
        print(str(max(m)+2 - r).zfill(2), end = ' ')
        for c in range(n) :
            if m[c] < max(m)+2 - r :
                print('..',end = ' ')
            else :
                print('##',end = ' ')
        print()
    for i in range(n+1):
        print(str(i).zfill(2),end = ' ')
if __name__ == '__main__' :
    main()