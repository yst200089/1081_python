#繪圖工具
import matplotlib.pyplot as plt
import math
# Sierpinski triangle
# x, y : 三角形的左下角座標
# l : 三角形的邊長
def triangle(x, y, l, xlist, ylist):
    # only one point
    if l <= 1 :
        xlist.append(x)
        ylist.append(y)
        return
    #由三個更小的三角形組成
    triangle(x, y, l//2, xlist, ylist)
    triangle(x + l//2, y, l//2, xlist, ylist)
    # sin60 = math.sin(math.pi/3)
    triangle(x + l//4, y + math.sin(math.pi/3)*l/2, l//2, xlist, ylist)
def main():
    # set the x limits of the current axes
    plt.xlim(0, 300)
    # set the y limits of the current axes
    plt.ylim(0, 300)
    xlist, ylist = [], []
    triangle(10, 10, 256, xlist, ylist)
    plt.plot(xlist, ylist, markersize = 1)
    plt.show()
if __name__ == "__main__" :
    main()