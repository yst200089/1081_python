#學號：108213052
#姓名：楊心慈
#input an int n
# print square of size n
# eg n == 5
#    *
#   ***
#  *****
# *******
#*********
# *******
#  *****
#   ***
#    *
# how ti think?
# (1) how many lines? n
# (2) if we give each line with id 'lineNum', then
# line 1: n-1 ' ' + 2n-1 個'*'
# line 2: n-2 ' ' + 2n-1 個'*'
# line lineNum: n-lineNum ' ' +2lineNum-1個'*'
def main():
    n = int(input())
    lineNum = 1
    while lineNum <= n :
        print(' ' * (n-lineNum) + '*'*((2*lineNum)-1))
        lineNum = lineNum + 1
    while lineNum > n and lineNum <= (2*n-1):
        print(' ' * (lineNum-n) + '*'*(((2*n)-1)+((-2)*(lineNum-n))))
        lineNum = lineNum + 1
if __name__ == '__main__' :
    main()
#最後修改：2019年9月16日22:14