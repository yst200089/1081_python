#學號：108213052
#姓名：楊心慈
def main():
    #輸入有幾堆方塊酥
    n = int(input())
    #輸入各堆方塊酥的數量
    scores = list(map(int,input().split()))
    sum = 0
    num = 0
    while num < n :
        #加總所有數字
        sum += scores[num]
        num += 1
    #算出平均
    avg = sum // n
    total = 0
    for i in scores:
        if i > avg :
            #算出多的方塊酥
            total += (i-avg)
    print(total)
if __name__ == '__main__' :
    main()
#最後修改：2019年10月24日15:55