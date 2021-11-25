#學號：108213052
#姓名：楊心慈
def comb(result, choice):
    #當手牌加底牌總共有五張
    if len(result) == 5 :
        printCard(result)
        #如果有4張相同號碼的牌
        if fourOfAKind(result):
            print('Player got     Four of a Kind')
        #如果有5張相同花色的牌
        elif flush(result):
            print('Player got     Flush')
        else :
            print('Player got     High card')
        return
    #做選牌的組合
    for i in range(len(choice)):
        comb(result+[choice[i]], choice[i+1:])
def printCard(result):
    #總共有C,D,H,S四個花色，以及13張號碼牌
    color, num = ['C', 'D', 'H', 'S'], ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    #輸出所選擇的牌
    print('Player choose ',*[color[h // 13] + num[h % 13]for h in result])
def fourOfAKind(result):
    #分出牌的號碼
    handNum = [h % 13 for h in result]
    #如果有4張相同號碼的牌
    if 4 in [handNum.count(h) for h in handNum]:
        return True
def flush(result):
    #分出牌的花色
    handColor = [h // 13 for h in result]
    #如果有5張相同花色的牌
    if 5 in [handColor.count(h) for h in handColor]:
        return True
def main():
    #輸入依序手牌和底牌的數量
    n, m = map(int,input().split())
    #依序輸入手牌
    hand = []
    for i in range(n):
        hand.append(int(input()))
    #依序輸入底牌
    under = []
    for v in range(m):
        under.append(int(input()))
    comb(hand, under)
if __name__=='__main__':
    main()
#最後修改：2019年12月23日10:14