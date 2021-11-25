# define a function to check if y is a leap year
def isLeap(y) :
    return y % 400 == 0 or (y%4==0 and y%100!=0)
def main():
    y = int(input())
    if isLeap(y) :
        print('leap year')
    else :
        print('common year')
if __name__ == '__main__' :
    main()