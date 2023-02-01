t = int(input())
for i in range(t):
    x, y = map(int, input().split())

    top10 = x * 10
    othr = y * 90
    print(top10 + othr)
