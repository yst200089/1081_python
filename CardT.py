# (1)花色 'SA'
# (2)大小
# (3)排序
# if you use str then
# 'S14' 'S13' 'S12' 'S11' 'S10' 'S9' 'S8' ... 'S2'
#I will use list of int, from 0 ~ 51
# SA ~ S2 : 0 ~ 12
# HA ~ H2 : 13 ~ 25
# DA ~ D2 : 26 ~ 38
# CA ~ C2 : 39 ~ 51
# for any card x between (0,51)
# x的花色是 x // 13
# x的大小是 x % 13
# x的排序, 就是整數的排序
import random
def myPrint(cards):
    cards.sort()
    colorName = ['S', 'H', 'D', 'C']
    seqName = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    # 印出四個花色，各自獨立一行
    for i in range(4):
        print(colorName[i], end = ' ')
        #
        for v in cards:
            if v // 13 == i:
                print(seqName[v % 13], end = '')
        # j = 0
        # for i in range(4) : # 印出四個花色, 各自獨立一行
        #     print(colorName[i], end = ' ')
        #     while cards[j] // 13 == i :
        #         print(seqName[cards[j]%13], end='')
        #         j += 1
        # 與 21 ~ 25 行功能相同 
        # 但執行時間從 n^4 變 n
        print()
def main():
    # 產生 52張牌
    cards = [i for i in range(52)]
    # 洗牌
    random.shuffle(cards)
    # tuple
    # playerName = ('South', 'West', 'North', 'East')
    playerName = ['North', 'East', 'South', 'West']
    # 發四家牌並印出來
    for i in range(4):
        # 印出玩家名字
        print(playerName[i])
        # 發牌並印出
        myPrint(cards[i*13: i*13+13])
if __name__ == '__main__' :
    main()