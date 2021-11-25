#學號：108213052
#姓名：楊心慈
#繪圖工具
import matplotlib.pyplot as plt
import math
# x, y : 起點座標
# d : 角度，使用360度
# l : 線段長度
# x + math.cos(math.radians(d))*l, y + math.sin(math.pi*d/180)*l
def line(x, y, d, l,xlist, ylist):
    # only one point
    if l <= 1 :
        xlist.append(x)
        ylist.append(y)
        return
    # line1 由組成
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
    # set the x limits of the current axes
    plt.xlim(0, 400)
    # set the y limits of the current axes
    plt.ylim(0, 400)
    xlist, ylist = [], []
    line(10, 250, 0, 243, xlist, ylist)
    plt.plot(xlist, ylist,'-')
    plt.show()
if __name__ == "__main__" :
    main()
#最後修改：2019年10月22日19:01