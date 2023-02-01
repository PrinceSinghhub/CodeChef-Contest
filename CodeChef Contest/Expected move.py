t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    ans = (x - 1) * (2 * y - x)
    print(ans)