def solve(x,y):
    if x == y:
        return 0

    elif x < y:
        return y - x

    else:
        if x % 2 == 0 and y % 2 == 0 or x % 2 != 0 and y % 2 != 0:
            return (x - y) // 2

        else:
            if x % 2 != 0 and y % 2 == 0 or x % 2 == 0 and y % 2 != 0:
                return ((x + 1 - y) // 2) + 1



t = int(input())

for i in range(t):

    x,y = map(int,input().split())

    print(solve(x,y))
