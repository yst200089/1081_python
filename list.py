#1
#1 1
#1 2 1
#1 3 3 1
#1 4 6 4 1
#第0個colume 都是1
#對角線都是1
#除了(1)(2)外的元素其值都次“正上”+“左上”
def genPascal(n):
    result=[[1 for j in range(i+1)] for i in range (n)]
    # except colume and diagonal
    #row 0 and row 1 都是1，不用處理
    #r = row , c = colume
    for r in range(2,n):
        #最左邊和最右邊的1不能動
        for c in range(1,r):
            result[r][c]=result[r-1][c]+result[r-1][c-1]
    return result
def myprint(result):
    for r in result:
        for c in r:
            print('{:2d}'.format(c),end='')
        print()
def main():
    myprint(genPascal(int(input())))
if __name__ == "__main__" :
    main()