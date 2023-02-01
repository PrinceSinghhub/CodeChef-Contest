t = int(input())
for i in range(t):

    n = int(input())

    deg = list(map(int, input().split()))

    if len(deg) < 2:
        print(0)
        continue

    while deg[-1] == 0:
        deg.pop()
    # print(deg)
    print(len(deg) - 1)