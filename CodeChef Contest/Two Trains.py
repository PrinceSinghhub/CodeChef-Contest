t = int(input())
for _ in range(t):
    N = int(input())
    stn = list(map(int,input().split()))
    ans = sum(stn)+max(stn)
    print(ans)