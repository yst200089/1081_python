#學號：108213052
#姓名：楊心慈
import random
def main():
    #輸入自己的號碼
    num = list(map(int,input().split()))
    #輸出開獎的號碼
    balls = [i for i in range(1,39)]
    #洗球
    random.shuffle(balls)
    #取前面六顆球
    lottery = balls[0:6]
    #將號碼由小到大排列
    lottery.sort()
    #輸出lottery
    print('lottery:',end='')
    for t in lottery :
        print(' '+'{:02}'.format(t),end='')
    print()
    #輸出中獎的號碼，排序由小到大
    winning=[]
    #比對lottery的每個數
    for i in lottery :
        #比對num的每個數
        for j in num :
            #如果等於就複寫在winning
            if i == j :
                winning.append(i)
    winning.sort()
    print('winning:',end='')
    for v in winning :
        print(' '+'{:02}'.format(v),end='')
    print()
if __name__ == '__main__' :
    main()
#最後修改：2019年10月17日20:56