# 123456 0
# 12345  6
# 1234  65
# 123  654
# 12  6543
# 1  65432
# 0 654321
def reverseInt(x):
    #反轉的結果
    y= 0
    #當x還有數字可以拿
    while x!= 0 :
        #拿出x的最後一個數字，放到y後面
        y= 10 * y+ x % 10
        #移走x的最後一個數字
        x = x // 10
    return y
def reverseStr(s):
    result= ''
    #for rach char c in string s 
    for c in s:
        #last to front
        result = c + result
    return result
def findSol(num):
    #do reverse and add until num is 'palindrome'
    #how to 'reverse' 'add'?
    num = num + reverseStr(num)
    add = 1
    #while not palindrome
    while num != reverseStr(num) :
        num = num + reverseStr(num)
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
if __name__ == "__main__" :
    main()