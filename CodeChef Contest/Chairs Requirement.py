t = int(input())
for _ in range(t):

    X, Y = map(int, input().split())

    if Y <= X:
        print(X - Y)

    else:
        print(0)