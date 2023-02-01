t = int(input())

for i in range(t):

    x,y = map(int,input().split())

    if x % 2 ==0:
        print("YES")

    else:
        if y == 1:
            print("YES")
        else:
            print("NO")
