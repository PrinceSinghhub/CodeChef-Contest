t = int(input())

for i in range(t):
    x,y,z = map(int, input().split())
    x = x*5
    y = y*10

    total = x + y
    # print(total)

    print(total//z)




