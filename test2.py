#學號：108213052
#姓名：楊心慈
# money : 金錢預算
# lower : 熱量下限
# upper : 熱量上限
# moneyList : 每種食物的價錢
# foodList :每種食物的熱量
# result : 已經選好的食物清單
# total : 已經選好的食物總熱量
def myfind(money, lower, upper, moneyList, foodList, result, total):
    #超過預算或超過熱量上限
    if money < 0 or total > upper :
        return
    #未達到熱量下限
    if total >= lower :
        #輸出已經選好的食物清單
        print(*result)
        #輸出已經選好的食物總熱量
        print(total)
        #因為是範圍，所以不用return
    #選第i種食物
    for i in range(len(moneyList)):
        myfind(money-moneyList[i], lower, upper,
               moneyList[i+1:], foodList[i+1:], 
               result+[foodList[i]], total+foodList[i])
def findSol(money, lower, upper, moneyList, foodList):
    myfind(money, lower, upper, moneyList, foodList, [], 0)
def main():
    #依序輸入預算、熱量範圍和幾種食物
    money, lower, upper, k = map(int,input().split())
    foodList = []
    moneyList = []
    for i in range(k):
        #輸入價錢與食物熱量
        x, y = map(int,input().split())
        moneyList.append(x)
        foodList.append(y)
    findSol(money, lower, upper, moneyList, foodList)
if __name__ == '__main__' :
    main()
#最後修改：2019年12月09日09:55