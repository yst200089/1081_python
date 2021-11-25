#學號：108213052
#姓名：楊心慈
def Buy(data,ins): # 買 # b 行為日期 消費金額（每5塊錢一點，無條件進位）
    if int(ins[2]) % 5 != 0: #（每5塊錢一點，無條件進位）
        data[int(ins[1][0:4])-1940+2][1] +=int(ins[2])//5 + 1 # 點數加在後 2 年 ( 點數有效期限 2 年 )
    else:
        data[int(ins[1][0:4])-1940+2][1] +=int(ins[2])//5 # 點數加在後 2 年 ( 點數有效期限 2 年 )
def Swap(data,ins): # 換點數 # s 行為日期 換掉的點數
    tmp = int(ins[1][0:4]) # 該年
    ins[2] = int(ins[2]) # 要換的點數
    while ins[2] > 0 : # 要換的點數 > 0，繼續執行
        if ins[2] > data[tmp-1940][1] : # 要換的點數 > 該年剩的點數
            ins[2] -= data[tmp-1940][1] # 還沒換的點數
            data[tmp-1940][1]=0 # 該年點數歸 0
            tmp += 1 # 換下一年換點數
        else:
            data[tmp-1940][1] -= ins[2] # 扣掉那年點數
            ins[2]=0 # 要換的點數歸 0
def Lookup(data,ins): # 查詢 # l 行為日期 # 只有輸入 l 才有輸出
    print(*data[int(ins[1][0:4])-1940]) # 印出後三年點數狀況
    print(*data[int(ins[1][0:4])-1940+1])
    print(*data[int(ins[1][0:4])-1940+2])
def main():
    data=[[i,0]for i in range(1940,2048)] # 原有的(年份,點數)點數
    for x in range(3): # 最開始有三行代表目前有的點數
        year,point=map(int,input().split()) # 輸入"過期年份 點數"
        data[year-1940][1]+=point # 將輸入的資料放入相對應年份的 list 中
    n =int(input()) # 輸入n(代表等下輸入n行)
    ins=[] # 指令
    for i in range(n): # 依序輸入 n 個指令
        ins.append(input().split()) # 指令
    # for i in range(n): # 依序檢查每個指令
        if ins[i][0] == 'b' : # 指令為 b
            Buy(data,ins[i]) # 執行 Buy
        elif ins[i][0] == 's' : # 指令為 s
            Swap(data,ins[i]) # 執行 Swap
        else : # 其餘
            Lookup(data,ins[i]) # 執行 Lookup
if __name__=='__main__':
    main()
#最後修改：2019年12月12日