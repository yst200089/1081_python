#read in n,then read in n float
#cal avg and stddev
def main():
    data = list()
    n = int(input())
    num = 0
    while num < n:
        data.append(float(input()))
        num += 1
    #加總所有數字
    sum = 0
    num = 0
    while num < n:
        sum += data[num]
        num += 1
    avg = sum  / n
    #加總所有(x-avg)**2
    sum=0
    num=0
    while num < n:
        sum = sum+(avg-data[num])**2
        num=num+1
    print(avg,(sum/n)**0.5)
if __name__ == '__main__':
    main()