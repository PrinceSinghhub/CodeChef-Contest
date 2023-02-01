def sumOfSubarrayProd(arr, n):
    ans = 0
    res = 0
    i = n - 1
    while (i >= 0):
        incr = arr[i] * (1 + res)
        ans += incr
        res = incr
        i -= 1
    return ans


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = sumOfSubarrayProd(arr, n)
    print(ans)