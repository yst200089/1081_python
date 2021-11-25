#學號：108213052
#姓名：楊心慈
#首先印出九宮格的狀態，接著讓玩家投球
#玩家一共有 9 次投球的機會，投完 9 次之後顯示遊戲結束。
#每球的命中率為 1/2
#被擊中的格子顯示為 0
#擊中的格子不能再投
import random
def printCube(board):
    for i in range(9) :
        if i != 0 and i % 3 == 0 :
            print()
        print('{:2d}'.format(board[i]),end = '' )
    print()
def play(board):
    #剩餘投球次數
    chance = 9
    #先印出九宮格初始狀態
    printCube(board)
    #當遊戲還沒結束，就繼續玩
    while chance > 0 :
        #印出"請選擇要投哪格"
        #輸入要投的位置
        target = int(input('請選擇要投哪格')) - 1
        #檢查是否合法，不合法就重新輸入
        while board[target] == 0 :
            target = int(input('已經投過，請重新選擇要投哪格')) - 1
        #合法則檢查是否擊中，並且減掉投球機會一次
        chance = chance - 1
        hit_or_not = random.randint(0, 1)
        #若擊中，則改變board狀態
        if hit_or_not == 1 :
            board[target] = 0
            print('擊中!!')
        else :
            print('失誤')
        #印出九宮格
        printCube(board)
    print('遊戲結束')
def main():
    #建立九宮格並填入數字
    board = [i + 1 for i in range(9)]
    #play game
    play(board)
if __name__ == '__main__' :
    main()
#最後修改：2019年10月07日12:02