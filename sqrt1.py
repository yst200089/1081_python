#二元逼近法
#目標是求一個值，但找不到方法(不知怎麼算)
#但存在可以測試對不對，或差多少的方法
# x >= 0
def sqrt(x):
    #x^0,5 will between(1,x)
    left, right = 1, x
    if x < 1 :
        left, right= x, 1
    mid = (left+right) / 2
    while left < mid and mid < right :
        if mid * mid > x : #mid在x的右邊
            right = mid
        else :
            left = mid
        mid = (left+right) / 2
    return mid
def main():
    x=float(input())
    print(sqrt(x))
if __name__ == '__main__' :
    main()