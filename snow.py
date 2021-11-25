#學號：108213052
#姓名：楊心慈
#繪圖工具
import matplotlib.pyplot as plt
import math
# x, y : 起點座標
# d : 角度(使用360度)
# l : 線段長度
def line(x, y, d, l,xlist, ylist):
    # 只有一點
    if l <= 1 :
        xlist.append(x)
        ylist.append(y)
        return
    # line1 由 4 條小線組成
    #第一條小線
    line(x, y, d, l//3, xlist, ylist)
    #第二條小線
    offx = math.cos(math.radians(d))*l/3
    offy = math.sin(math.radians(d))*l/3
    line(x + offx, y + offy, d + 60, l//3, xlist, ylist)
    #第三條小線
    offx = math.cos(math.radians(d))*l/3 + math.cos(math.radians(d+60))*l/3
    offy = math.sin(math.radians(d))*l/3 + math.sin(math.radians(d+60))*l/3
    line(x + offx, y + offy, d - 60, l//3, xlist, ylist)
    #第四條小線
    offx = math.cos(math.radians(d))*l/3*2
    offy = math.sin(math.radians(d))*l/3*2
    line(x + offx, y + offy, d, l//3, xlist, ylist)
def main():
    # 設定 x 軸的範圍
    plt.xlim(0, 400)
    # 設定 y 軸的範圍
    plt.ylim(0, 400)
    xlist, ylist = [], []
    #中上的線
    line(0, 250, 0, 243, xlist, ylist)
    #右下的線
    line(243, 250, -120, 243, xlist, ylist)
    #左上的線
    line(243/2, 250-243/2*(3**0.5), 120, 243, xlist, ylist)
    plt.plot(xlist, ylist,'-')
    plt.show()
if __name__ == "__main__" :
    main()
#最後修改：2019年11月10日12:15