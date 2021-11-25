# x is list
def minMax(x):
    min, max = x[0],x[0]
    for v in x[1:]:
        if min > v :
            min = v
        if max < v :
            max = v
    return min, max
    #return min
def main():
    data = list(map(float,input().split()))
    a,b=minMax(data)
    print(a,b)
if __name__ == '__main__' :
    main()