#對一個n皇后問題
#用n*n的矩陣來代表
#一共有n條直線，n條橫線，2n-1條右上斜線，2n-1條右下斜線
#如果我們用0~n-1直線，0~n-1代表n條橫線，以及0~2n-2代表某一條右上右下斜線
#請問若皇后佔住(r,c)這個位置，則此皇后佔住了哪幾條線？
#(1)編號是r的橫線
#(2)編號是c的直線
#(3)編號是r+c的右上斜線
#(4)編號是r-c+(n-1)的右下斜線
# n : 一共要放幾個皇后
# board : 棋盤
# row : 負責放哪個row的皇后
# straightFree : 直線是否可放
# uprightFree : 右上斜線是否可放
# downrightFree : 右上斜線是否可放
def myqueen(n, board, row, straightFree, uprightFree, downrightFree):
    #計算一輪結束
    if row == n :
        #印出結果
        for r in board :
            print(*r)
        #分隔每個結果
        print("*"*(2*n-1))
        return
    for col in range(n) :
        if straightFree[col] and uprightFree[row+col] and downrightFree[row-col+n-1]:
            #當直線、右上斜線和右下斜線為Ture，印出'Q'
            board[row][col] = 'Q'
            #將'Q'周遭的直線、右上斜線和右下斜線則改為False
            straightFree[col] = uprightFree[row+col] = downrightFree[row-col+n-1] = False
            #換下一個row
            myqueen(n, board, row+1, straightFree, uprightFree, downrightFree)
            #一輪結束後，重整成'.'
            board[row][col] = '.'
            #一輪結束後，重整成True
            straightFree[col] = uprightFree[row+col] = downrightFree[row-col+n-1] = True
def queen(n):
    #執行
    myqueen(n, [[ '.' for c in range(n)] for r in range(n)], 0, \
            [True for i in range(n)], [True for i in range(2*n-1)], [True for i in range(2*n-1)])
def main():
    #有n個皇后
    n = int(input())
    #執行
    queen(n)
if __name__ == '__main__' :
    main()