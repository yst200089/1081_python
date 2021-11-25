#繪圖工具
import matplotlib.pyplot as plt
import math
def square(x, y, l, xlist, ylist):
    # only one point
    if l <= 1 :
        xlist.append(x)
        ylist.append(y)
        return
    #由三個更小的三角形組成
    square(x , y , l//3, xlist, ylist) #左下
    square(x, y + l//3, l//3, xlist, ylist) #左中
    square(x, y + (l//3)*2, l//3, xlist, ylist) #左上
    square(x + l//3, y + (l//3)*2, l//3, xlist, ylist) #中上
    square(x + (l//3)*2, y + (l//3)*2, l//3, xlist, ylist) #右上
    square(x + (l//3)*2, y + l//3, l//3, xlist, ylist) #右中
    square(x + (l//3)*2, y, l//3, xlist, ylist) #右下
    square(x + l//3, y, l//3,xlist, ylist) #中下
def main():
    # set the x limits of the current axes
    plt.xlim(0, 300)
    # set the y limits of the current axes
    plt.ylim(0, 300)
    xlist, ylist = [], []
    square(10, 10, 243, xlist, ylist)
    plt.plot(xlist, ylist, markersize = 1)
    plt.show()
if __name__ == "__main__" :
    main()