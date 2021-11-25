# 麻將一共有34種牌
# 1~9萬、1~9筒、1~9條
# 東南西北中發白
# 台灣麻將一開始發16張牌，摸一張變17張牌，若這17張牌可以'組合'成如下即可胡牌:
# (1)有麻將，意指兩張一樣的牌
# (2)其餘15張，可以組成5組的'刻'(3張一樣的)或'順'(萬條筒連號)
# 題目是，給34介於0~4的int，且其總和為17，寫一函數判斷能否胡牌
# 0~8，表示1~9萬
# 9~17，表示1~9筒
# 18~26，表示1~9條
# 27~33，表示東南西北中發白
# 如何判斷是否為'萬條筒'? x<27
# 已知是萬筒條，判斷是哪一種? x//9
# 以知是萬筒條，求大小? x%9

#cards : 每一種牌的張數，0~4
#n : 還有幾張要選
def myCanHu(cards, n):
    #如果胡了
    if n == 0 :
        return True
    result = False
    for i in range(34):
        # 麻將
        #沒選過麻將，且這張牌可以當麻將
        if n % 3 != 0 and cards[i] >= 2 :
            #複製一份給同學，不要讓同學動到我手上的牌
            remain = cards[::]
            #給同學的牌要扣掉兩張當麻將的
            remain[i] -= 2
            #問同學剩下的可以胡嗎?
            if myCardHu(remain, n-2):
                result = True
        # 刻
        if cards[i] >= 3 :
            remain = cards[::]
            remain[i] -= 3
            if myCardHu(remain, n-3):
                result = True
        # 順 
        if x < 27 and i % 9 < 7 and cards[i] >= 1 and cards[i+1] >= 1 and cards[i+2] >= 1 :
        remain = cards[::]
        remain[i] -= 1
        remain[i+1] -= 1
        remain[i+2] -= 1
        if myCardHu(remain, n-3):
                result = True
    return result
def canHu(cards):
    return myCacHu(cards, 17)
def main():
    majon = ['一萬','二萬','三萬','四萬','五萬','六萬','七萬','八萬','九萬', \
        '一筒','二筒','三筒','四筒','五筒','六筒','七筒','八筒','九筒', \
        '一條','二條','三條','四條','五條','六條','七條','八條','九條','東','南','西','北','中','發','白']
    cards = list(map(int,input().split()))
    print(canHu(cards))
if __name__ == '__main__' :
    main()