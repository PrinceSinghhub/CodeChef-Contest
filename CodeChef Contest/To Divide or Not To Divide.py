t = int(input())
x = 0
for _ in range(t):
    a, b, n = map(int, input().split())
    if a % b == 0:
        print(-1)
        continue

    x = n
    if (x % a != 0):
        x = n + a - (x % a)
    while not (x % a == 0 and x % b != 0):
        x += a
    print(x)