# 寫recursion程式，請永遠記住三步驟
# (1)函數的規格(參數)
# (2)完成(終止)條件
# (3)化簡(呼叫自己)的方法
# 以費氏數為例
# (1)參數n代表費氏數列的第n項
# (2)完成條件，當n<=1時，其值為n
# (3)化簡方法，F(n-1)+F(n-2)
# 費氏數列F(n)的定義
# if n <= 1 then n
# otherwise F(n-1)+F(n-1)
def F(n):
    if n <= 1:
        return n 
    return F(n-1)+F(n-2)
def main():
    n = int(input())
    print(F(n))
if __name__ == '__main__' :
    main()