t = int(input())
for _ in range(t):

    X, Y = map(int, input().split())

    total = X * 4

    if X > Y:
        total += Y
        print(total)
    else:
        print(total)
