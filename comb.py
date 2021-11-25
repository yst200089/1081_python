# 組合問題
# n個元素取出m個
# (A,B,C,D,E) choose 2 elements
# 你有5種選法
# 選A，剩下(B,C,D,E)4選1個
# 選B，剩下(C,D,E)3選1個
# 選C，剩下(D,E)2選1個
# 選D，剩下(E)1選1個
# 選E，剩下()0選1個

def comb(data, m, result):
    #完成條件？
    if m == 0 :
        #result : 前面的人已經選了哪幾個
        print(*result)
        return
    for i in range(len(data)) :
        comb(data[i+1:], m-1, result+ [data[i]])
def main():
    #data : 有哪些元素要選
    data = input().split()
    #m : 要選幾個
    m = int(input())
    comb(data, m, [])
if __name__ == '__main__' :
    main()