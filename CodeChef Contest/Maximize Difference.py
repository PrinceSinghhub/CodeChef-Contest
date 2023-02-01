import sys

MIN_INT = -sys.maxsize-1
t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    a = 0
    b = 0

    if m < (2*n):
        print(m,m)

    elif m % n == 0:
        print(m,n)

    else:
        x = m/2
        if m >=(2*n):
            x = 2*n
        diff = MIN_INT
        for i in range(n,x):
            d = int(m/i)
            dd = int(i*d)-i
            if dd > diff:
                a = i
                b = i*d
                diff = dd
            n+=1
        print(a,b)
