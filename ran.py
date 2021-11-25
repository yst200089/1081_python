#學號：108213052
#姓名：楊心慈
#先在1到38之間找出六個數
#比大小，由小到大排列
import random
def main():
    num = [i for i in range(1,38)]
    result=random.sample(num,6)
    result.sort()
    print (result)
if __name__ == '__main__' :
    main()
#最後修改：2019年9月30日14:21