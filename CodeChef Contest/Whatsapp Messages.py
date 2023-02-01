t = int(input())

for i in range(t):
    x, y, z = map(int, input().split())

    remain = x - y

    print(remain * z)