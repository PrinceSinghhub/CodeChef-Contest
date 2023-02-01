t = int(input())
for i in range(t):
    x,y = map(int,input().split())

    arr = [i for i in range(min(x,y),max(x,y)+1)]
    ans = len(arr)-2
    ans = (ans//2)+1
    print(ans)