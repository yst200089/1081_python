def findNum(data, m, result):
    if m == 0 :
        line_1 = result[0]*10+result[1]
        line_2 = result[2]
        line_3 = result[3]*10+result[4]
        line_4 = result[5]*10+result[6]
        line_5 = result[7]*10+result[8]
        if line_1 * line_2 == line_3 and \
           line_3 + line_4 == line_5 :
            print(*result)
        return
    for i in range(len(data)):
        findNum(data[:i]+data[i+1:], m-1, result+[data[i]])
def main():
    # 總共有0,1,2,3,4,5,6,7,8,9個數字
    findNum([i+1 for i in range(9)], 9, [])
if __name__ == '__main__' :
    main()