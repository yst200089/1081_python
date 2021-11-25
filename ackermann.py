#A(m,n) = n+1,if m = 0
#       = A(m-1,1) if m>0 and n=0
#       = A(m-1,A(m,n-1)) if m>0 and n>0
def A(m,n):
    if m == 0:
        return n+1
    elif n == 0:
        return A(m-1,1)
    else :
        return A(m-1,A(m,n-1))
def main():
    m,n = int(input())
    print(A(m,n))
if __name__ == '__main__' :
    main()