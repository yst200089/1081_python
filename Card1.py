#學號：108213052
#姓名：楊心慈
import random
#總共有52張牌
card = list(range(52))
#洗牌
random.shuffle(card) 
def myCards(n):
    #總共有13張撲克牌
    Num=['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    return Num[n]
#發牌給四位玩家，
player = [ [],[],[],[] ]
#分別是['North','East','South','West']
each = ['North','East','South','West']
def shuffle(each,card):
    #將52張牌分成四個玩家
    for i in range(4): 
        player[i] = card[i*13: 13+i*13 ] 
        #將玩家的牌，由大到小依序排列
        player[i].sort(reverse = True)
        #定義四個花色
        S = [] 
        H = [] 
        D = [] 
        C = []  
        for j in range(13): 
            #數字39~52為黑桃
            if player[i][j] > 38: 
                S.insert(0,myCards(player[i][j] - 39))
            #數字26~38為愛心
            elif player[i][j] > 25: 
                H.insert(0,myCards(player[i][j]-26)) 
            #數字13~25為菱形
            elif player[i][j] > 12: 
                D.insert(0,myCards(player[i][j] - 13))
            #數字0~12為梅花
            else: 
                C.insert(0,myCards(player[i][j]))
        #輸出玩家以及每個人所發到的牌
        print(each[i]+':') 
        print('S',''.join(S)) 
        print('H',''.join(H)) 
        print('D',''.join(D)) 
        print('C',''.join(C))
def main():
    shuffle(each,card)
if __name__ == '__main__' :
    main()
#最後修改：2019年10月07日20:03