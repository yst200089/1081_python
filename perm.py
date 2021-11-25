# 排列(都不能重複)
# 組合(排序不能重複，但號碼組合重複)
def comb(data, m, result):
    if m == 0 :
        print(*result)
        return
    for i in range(len(data)) :
        # 每個位置都有機會被選一次
        comb(data[i+1:], m-1, result+[data[i]])
def perm(data, m, result):
    if m == 0 :
        print(*result)
        return
    for i in range(len(data)) :
        # 每個位置都有機會被選一次
        perm(data[:i]+data[i+1:], m-1, result+[data[i]])
def main():
    data = input().split()
    m = int(input())
    comb(data, m, [])
    perm(data, m, [])
if __name__ == '__main__' :
    main()