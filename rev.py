def findSol(num):
    #do reverse and add until num is 'palindrome'
    #how to 'reverse' 'add'?
    num = str(int(num) + int(num[::-1]))
    add = 1
    #while not palindrome
    while num != num[::-1] :
        num = str(int(num) + int(num[::-1]))
        add += 1
    #加了幾次，最後的迴文
    return add, num
def main():
    #read in how many lines in input
    n = int(input())
    for i in range(n) :
        #read in eachline 一行一個數字
        add, result = findSol(input())
        print(add,result)
if __name__ == '__main__' :
    main()