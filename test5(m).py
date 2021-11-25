#學號：108213052
#姓名：楊心慈
def myboard(n, x, result, data):
    for i in range(len(data)):
        for v in range(x-data[i]):
            result[v][i] = '..'
    myprint(result, x, n)
def myprint(result, x, n):
    i = x
    for r in result:
        #印出列數
        print('{:02}'.format(i),end=' ')
        i -= 1
        #印出內容
        for c in r:
            print(c,end=' ')
        print()
    #印出行數
    for v in range(n+1):
        print('{:02}'.format(v),end=' ')
    print()
def board(n, x, data):
    #印出版面
    myboard(n, x, [[ "##" for c in range(n)] for r in range(x)], data)
def main():
    #輸入要印在長條圖上的數字
    n = int(input())
    #在長條圖上顯示的數值
    data = list(map(int,input().split()))
    #找出最大值
    max = -1
    for i in data :
        if i > max :
            max = i
    board(n, max+2, data)
if __name__=='__main__':
    main()
#最後修改：2019年12月26日22:10