#學號：108213052
#姓名：楊心慈
def isPrime(n):
    #num由 2 開始
    num = 2
    # 直到num 到 n-1
    while num < n :
        #若可以整除
        if n % num == 0 :
            #就不是質數
            return False
        #測試下一個數字
        num = num + 1
    #都不能整除，就是質數
    return True
def main() :
    prime = []
    n = int(input())
    count = 0
    for num in range(2,n+1):
        ##判斷n是不是質數
        if isPrime(num) :
            count += 1
            prime.append(num)
    #求出質數的階乘
    for i in prime :
        sum = 1
        for v in range(1,i + 1):
            sum *= v
        print('%s! ='%(i),end = ' ')
        #分別輸出質數的階乘
        print(sum)
    #輸出有多少質數
    print('factorial called',end = ' ')
    print(count,end = ' ')
    print('times')
if __name__ == '__main__' :
    main()
#最後修改：2019年10月23日23:01