def main():
    #學生總人數
    n = int(input())
    #輸入每個學生的成績
    data = list(map(float,input().split()))
    #加總所有數字
    sum = 0
    num = 0
    while num < n :
        sum += data[num]
        num += 1
    #算出平均
    avg =float(sum / n)
    print('average:',end='')
    print(avg)
    #算出比平均小的人數
    count = 0
    for i in data :
        if i < avg:
            count += 1
        num += 1
    print('num:',end='')
    print(count)
if __name__ == '__main__' :
    main()
#最後修改：2019年10月17日21:37
