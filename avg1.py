#read in n,then read in n float
#cal avg and stddev
def main():
    data = list()
    n = int(input())
    num = 0
    while num < n:
        data.append(float(input()))
        num +=1
    #加總所有數字
    sum = 0
    for x in data: #for each x in data
        sum += x
    avg = sum  / n
    #加總所有(x-avg)**2
    sum=0
    for x in data:
        sum = sum+(avg-x)**2
    print(avg,(sum/n)**0.5)
if __name__ == '__main__':
    main()