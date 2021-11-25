#學號：108213052
#姓名：楊心慈
def run(data, m, result):
    # 如果數字加起來等於 m ,輸出
    if m == 0 :
        print(*result)
        return
    # 將每個數排列
    for i in range(len(data)):
        run(data[i+1:], m-data[i], result+[data[i]])
def main():
    # n 個大一學生，老俞跑 m 距離
    m = int(input())
    # 每個學生能跑的距離
    data = list(map(int,input().split()))
    run(data, m, [])
if __name__ == '__main__' :
    main()
#最後修改：2019年10月31日17:44