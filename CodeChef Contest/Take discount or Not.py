t = int(input())

for i in range(t):

    N, X, Y = map(int, input().split())

    arr = list(map(int, input().split()))

    total = sum(arr)
    cuppon = X

    Sum = 0

    for i in arr:
        if i > Y:
            Sum += i - Y
        else:
            Sum += 0

    if Sum + cuppon < total:
        print("COUPON")

    else:
        print('NO COUPON')