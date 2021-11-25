#學號：108213052
#姓名：楊心慈
#先在1到38之間找出六個數
#比大小，由小到大排列
import random
def printgame(balls):
    #從38顆球裡取出6顆球
    for i in range(6):
        Num = balls[0:6]
        Num.sort()
        print(Num[i],end = ' ')
    #由小到大依序排列
def main():
    #總共有0~38個數
    balls = [i for i in range(1,39)]
    #洗球
    random.shuffle(balls)
    printgame(balls)
if __name__ == '__main__' :
    main()
#最後修改：2019年10月09日19:35