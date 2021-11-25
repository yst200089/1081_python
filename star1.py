#input an int n
# print square of size n
# eg n == 4
#⭐️
#⭐️⭐️
#⭐️⭐️⭐️
#⭐️⭐️⭐️⭐️
# how ti think?
# (1) how many lines? n
# (2) if we give each line with id 'lineNum', then
# line 1: how many ⭐️? 1
# line 2: how many ⭐️? 2
# line lineNum: how many ⭐️? lineNum
def main():
    n = int(input())
    lineNum = 1
    while lineNum <= n :
        print('*' * lineNum)
        lineNum = lineNum + 1
if __name__ == '__main__' :
    main()