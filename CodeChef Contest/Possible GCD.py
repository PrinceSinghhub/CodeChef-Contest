import math

t = int(input())
for _ in range(t):
    A, B = map(int, input().split())
    d = 0
    s = abs(A - B)
    t = math.sqrt(s)
    i = 1
    while i <= t:
        if s % i == 0:
            if s / i == i:
                d += 1
            else:
                d += 2
        i += 1
    print(d)


