# define a function to check if y is a leap year
def isLeap(y) :
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)
def countLeap(begin, end) :
    count = 0
    num = begin
    while num <= end :
        if isLeap(num) :
            count += 1
        num +=1
    return count
def main() :
    begin, end = map(int,input().split())
    print(countLeap(begin, end))
if __name__ == '__main__' :
    main()