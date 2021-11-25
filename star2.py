#input an int n
# print square of size n
# eg n == 4
#      ⭐️
#    ⭐️⭐️
#  ⭐️⭐️⭐️
#⭐️⭐️⭐️⭐️
# how ti think?
# (1) how many lines? n
# (2) if we give each line with id 'lineNum', then
# line 1: n-1 ' ' +1個'⭐️'
# line 2: n-2 ' ' +2個'⭐️'
# line lineNum: n-lineNum ' ' +lineNum個'⭐️'
def main():
    n = int(input())
    lineNum = 1
    while lineNum <= n :
        print(' ' * (n-lineNum) + '*'*lineNum)
        lineNum = lineNum + 1
if __name__ == '__main__' :
    main()