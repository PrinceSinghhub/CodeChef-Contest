t = int(input())
for _ in range(t):

    n = int(input())
    arr = [-1] * n
    arr[n - 1] = n
    k = n

    for i in range(1, n):

        if i % 2 != 0:
            arr[n - 1 - i] = (k - (n - i))
            k = arr[n - 1 - i]

        elif i % 2 == 0:
            arr[n - 1 - i] = (k + (n - i))
            k = arr[n - 1 - i]

    for i in range(n):
        print(arr[i], end=" ")
    print()
