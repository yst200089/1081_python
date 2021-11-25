#學號：108213052
#姓名：楊心慈
def mySquare(n):
    #輸入n會出現n*n正方形
    result = [[(i+1) for j in range(n)] for i in range(n)]
    #r =row ,c = colume
    for r in range(n):
        #右邊的第n行第n個內的數都不能動
        for c in range(r+1,n):
            #除了上面的數字之外，每一個數字都是左邊加一
            result[r][c]=result[r][c-1]+1
    return result
def myprint(result):
    for r in result:
        for c in r:
            print(format(c),end='   ')
        print()
def main():
    myprint(mySquare(int(input())))
if __name__ == '__main__':
    main()
#最後修改：2019年10月10日00:23