# 定義Hanoi函數的規格
# n : 有幾個disc要移動
# src : 來源柱子
# dest : 目的住
# third : 另一根柱子
# result : 每根柱子的disc號碼
# move n discs from scr to dest
def Hanoi(n, src, dest, third, result) :
    if n == 0 :
        print(*result[0])
        print(*result[1])
        print(*result[2])
        print('--------')
        return
    # move n-1 discs, from src to third
    Hanoi(n-1, src, third, dest, result)
    # move one discs, from src to dest
    result[dest].append(result[src].pop())
    # move n-1 discs, from third to dest
    Hanoi(n-1, third, dest, src, result)
def main():
    n = int(input())
    Hanoi(n, 0, 1, 2, [[n-i for i in range(n)],[],[]])
if __name__ == '__main__' :
    main()