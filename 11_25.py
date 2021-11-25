# 0  1  2  3  4  5  6  7  8
# 9 10 11 12 13 14 15 16 17
#數獨有81個格子要填入1~9
#橫列、直行、區塊內的數字不得重複
#假設我們0~80表示由上而下，由左至右的格子編號
# 0  1  2  3  4  5  6  7  8
# 9 10 11 12 13 14 15 16 17
#請問編號x在......
#哪條橫列？ x // 9
#哪條直行？ x % 9
#哪個區塊？ (x // 9)//3*3 + (x % 9)//3 = x//27*3+x%9//3
#區塊編號
# 0 1 2
# 3 4 5
# 6 7 8
#輸入：
#一行有81個0~9的整數，代表九宮格的81個數字，數字0表示空白沒指定，1~9表示只能填該數字
#輸出數獨的答案，9列每列9行

#broad : 81個數字，非0代表以確定只能填該數字
#rowNum : 某橫列還有哪些數字是可能的
#colNum : 某直行還有哪些數字是可能的
#blockNum : 某區塊還有哪些數字是可能的
def markKnown(board, rowNum, colNum, blockNum):
    #check each position
    for x in range(81):
        if board[x] != 0 :
            if board[x] in rowNum[x//9]:
                rowNum[x//9].remove(board[x])
            if board[x] in colNum[x%9]:
                colNum[x%9].remove(board[x])
            if board[x] in blockNum[x//27*3+x%9//3]:
                blockNum[x//27*3+x%9//3].remove(board[x])
#broad : 81個格子內的數字
#x : 要負責填幾個格子
#rowNum : 某橫列還有哪些數字是可能的
#colNum : 某直行還有哪些數字是可能的
#blockNum : 某區塊還有哪些數字是可能的
def fill(board, x, rowNum, colNum, blockNum):
    if x == 81 :
        for i in range(9):
            #印出9*9的答案
            print(*board[i*9:(i+1)*9])
        return
    # 已經確定的
    if board[x] != 0 :
        fill(board, x+1, rowNum, colNum, blockNum)
        return
    #1~9每個檢查一下能不能填
    for i in range(1, 10):
        if i in rowNum[x//9] and i in colNum[x%9] and i in blockNum[x//27*3+x%9//3]:
            rowNum[x//9].remove(i) # 移除已經有填過的數字
            colNum[x%9].remove(i)
            blockNum[x//27*3+x%9//3].remove(i)
            board[x] = i
            fill(board, x+1, rowNum, colNum, blockNum)
            rowNum[x//9].append(i)
            colNum[x%9].append(i)
            blockNum[x//27*3+x%9//3].append(i)
            board[x] = 0
def findSol(board):
    #有9個row，每個row一開始都可以填入1~9
    rowNum = [[1, 2, 3, 4, 5, 6, 7, 8, 9] for i in range(9)]
    #有9個col，每個col一開始都可以填入1~9
    colNum = [[1, 2, 3, 4, 5, 6, 7, 8, 9] for i in range(9)]
    #有9個block，每個block一開始都可以填入1~9
    blockNum = [[1, 2, 3, 4, 5, 6, 7, 8, 9] for i in range(9)]
    #先用已經確定的數字整理每個列行塊的數字
    markKnown(board, rowNum, colNum, blockNum)
    # call recurion function
    fill(board, 0, rowNum, colNum, blockNum)
def main():
    findSol(list(map(int,input().split())))
if __name__ == '__main__' :
    main()