#學號：108213052
#姓名：楊心慈
def func(price):
    count = 0
    #當價錢大於50時，數值加一
    while price > 50 :
        price = price * 0.5
        count += 1
    if price < 0 :
        count = 'error'
    print (count)
def main():
    #輸入加一
    price = int(input())
    func(price)
if __name__ == '__main__' :
    main()
#最後修改：2019年10月17日21:51