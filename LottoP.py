import random
def main():
    data = list(map(int,input().split()))
    allNum = [i for i in range(1,39)]
    random.shuffle(allNum)
    win = allNum[0:6]
    win.sort()
    match = []
    for v in win :
        if v in data :
            match.append(v)
    print(*allNum)
    print(*match)
if __name__ == '__main__' :
    main()