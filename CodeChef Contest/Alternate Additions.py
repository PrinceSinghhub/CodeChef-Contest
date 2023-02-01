t = int(input())
for _ in range(t):

    X, Y = map(int, input().split())

    if ((Y - X) % 3 == 0 or (Y - X) % 3 == 1):
        print('YES')
    else:
        print("NO")

