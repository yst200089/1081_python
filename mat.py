# row = 矩陣B的列
# coi = 每一列有c行
# m = 表示對矩陣A的操作
def main():
    #輸入 r, c, m 
    row, col, m = map(int,input().split())
    data = []
    #輸入矩陣B內容
    for i in range(row) :
        data.append(list(map(int,input().split())))
    #輸入對矩陣A進行的操作
    ops = list(map(int,input().split()))
    #反過來進行對矩陣A的操作
    ops.reverse()
    for op in ops :
        #m = 0,代表旋轉
        if op == 0 :
            #第一個索引代表結果的row
            #第二個索引代表結果的columns
            #要把原來的(r,col-1-c)移到(c,r)
            # (0,0)-->(1,0)
            # (0,1)-->(1,1)
            data = [[data[r][col-1-c] for r in range(row)] for c in range(col)]
            row, col = col, row
        #m = 1,代表翻轉
        else :
            data = [[data[row-1-r][c] for c in range(col)] for r in range(row)]
    #輸出矩陣A
    for r in  data :
        print(*r)
if __name__ == "__main__" :
    main()