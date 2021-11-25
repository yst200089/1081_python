#奇數魔方陣
# 17 24  1  8 15
# 23  5  7 14 16
#  4  6 13 20 22
# 10 12 19 21  3
# 11 18 25  2  9
def genMagic(n):
    #產生所有值為0的list of list
    data = [[0 for j in range(n)]for i in range(n)]
    #目前位置為 上方中間
    #在目前位置填入1
    curX, curY, data[curY][curX] = n//2, 0 ,1
    #接下來由2到n*n依序填入
    for v in range(2, n*n + 1) :
        # 找出下一個位置
        # 下一個位置是原來的右上方
        nextX , nextY = (curX+1) % n , (curY-1) % n
        # 如果下個位置有數字
        if data[nextY][nextX] != 0 :
            #設定下一個位置為現在位置的下方
            nextX, nextY = curX, curY+1
        # 填入數字
        # 把現在的位置改成下一個位置
        curX, curY, data[nextY][nextX] = nextX, nextY, v
    #傳回結果
    return data
def main():
    rel = genMagic(int(input()))
    for row in rel :
        print(*row)
if __name__ == '__main__' :
    main()