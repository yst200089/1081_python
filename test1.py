#學號：108213052
#姓名：楊心慈
def findSol(data, codebook):
    #如果字串選完
    if len(data) == 0 :
        return 1
    count = 0
    #檢查每一種編碼方式
    for code in codebook :
        #如果可以編碼
        if data.startswith(code):
            #繼續編碼剩下的資料
            count += findSol(data[len(code):],codebook)
    return count
def main():
    #輸入字串長度n與m種字元
    n, m = map(int,input().split())
    #輸入要寫的密碼字串
    data = input()
    #依序輸入a種字元
    codebook = []
    for i in range(m):
        codebook.append(input())
    #輸出有種組合
    print(findSol(data,codebook))
if __name__ == '__main__' :
    main()
#最後修改：2019年12月02日10:10