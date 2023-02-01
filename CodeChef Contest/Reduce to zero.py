import math

t = int(input())
for _ in range(t):

    X, Y = map(int, input().split())

    Max = max(X, Y)
    Sum = X + Y - Max

    if Sum != 0:
        count = int(math.log2(Max / Sum))

        a = Sum

        for i in range(count):
            a *= 2

        if a != Max:
            count += 1

        print(count + Max)

    elif Sum == 0 and Max == 0:
        print(0)

    else:
        print(-1)