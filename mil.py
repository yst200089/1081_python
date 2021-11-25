#學號：108213052
#姓名：楊心慈
def main():
    #輸入出生年、月、日
    a,b,c=map(int,input().split())
    #求出年/(月＋日)的商數
    q = a // (b + c)
    #求出年/(月＋日)的餘數
    r = a % (b + c)
    #當兵天數
    days = q + r + b + c
    print(days)
if __name__ == '__main__' :
    main()
#最後修改：2019年10月23日23:41