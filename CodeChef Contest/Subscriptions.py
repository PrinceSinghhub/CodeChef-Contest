import math

t = int(input())
for _ in range(t):

    X, Y = map(int, input().split())

    if X <= 6:
        print(Y)

    elif X % 6 == 0:
        print(((X // 6) * Y))

    else:
        X = math.ceil(X / 6)
        print(X * Y)