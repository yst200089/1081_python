#學號：108213052
#姓名：楊心慈
#input an int n
# print square of size n
# eg n == 4
#    *
#   ***
#  *****
# *******
def main():
    n = int(input())
    lineNum = 1
    #line lineNum: n-lineNum ' ' +lineNum個'*'
    while lineNum <= n :
        print(' ' * (n-lineNum) + '*'*((2*lineNum)-1))
        lineNum = lineNum + 1
if __name__ == '__main__' :
    main()
#最後修改：2019年9月30日11:40