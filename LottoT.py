# lotto兌獎
import random
def main():
    #read in user's number
    data = list(map(int,input().split()))
    #generate開獎號碼
    allNum = [i for i in range(1,39)]
    random.shuffle(allNum)
    win = allNum[0:6]
    win.sort()
    #找出哪幾個號碼一樣
    matched=[]
    for v in win :
        if v in data :
            matched.append(v)
    #print genrated numbers, and matched number
    print(*win)
    print(*matched)
if __name__ == '__main__' :
    main()
def main():
    # 1~38任取6個數字
    win = sorted(random.sample([i for i in range(1,39)],6))#取代˙7~11行
    print(*win)
    print('win:',*sorted([i for i in map(int,input().split()) if i in win]))
if __name__  == '__main__' :
    main()