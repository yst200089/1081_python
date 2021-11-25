#學號：108213052
#姓名：楊心慈
import random
def each(cards):
    #將52張牌分成四份
    for i in range(4):
        game = cards[i*13:i*13+13]
        #並把牌由大到小依序排列
        game.sort()
        #將分成四份的牌，依序發給North,East,South,West
        players = ['North','East','South','West']
        print(players[i]+':')
        myCards(game)
def myCards(game):
    #總共有S,H,D,C四個花色
    colors = ['S','H','D','C']
    #以及13張號碼牌
    Num = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    #定義商數代表的花色
    for i in range(4):
        print(colors[i],end=' ')
        #定義餘數代表的號碼
        for j in range(13):
            #將商數作為判斷花色的依據
            if game[j] // 13 == i :
                #將餘數作為判斷號碼的依據
                print(Num[game[j]%13],end='')
        print()
def main():
    #總共有52張牌
    cards = [i for i in range(52)]
    #洗牌
    random.shuffle(cards)
    #輸出四個玩家所發到的牌(包括其花色、號碼)
    each(cards)
if __name__ == '__main__':
    main()
#最後修改：2019年10月09日16:05