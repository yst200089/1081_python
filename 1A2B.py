#學號：108213052
#姓名：楊心慈
import random
def main():
    #輸入一組(4個)數字
    ans = input()
    #輸入要比對的數字
    n = 1
    while n <= 5:
        num = input()
        #比對兩組數字的位置以及數字
        A = 0
        B = 0
        for v in range(4):
            #如果數字和位置一樣A+1
            if ans[v] == num[v] :
                A += 1
            #如果數字一樣但位置不一樣B+1
            if num[v] in ans :
                B += 1
        #將重複的數字扣掉
        B = B-A
        print(A,end ='')
        print('A',end = '')
        print(B,end ='')
        print('B',end = '')
        n += 1
        print()
if __name__ == '__main__' :
    main()
#最後修改：2019年10月22日19:01