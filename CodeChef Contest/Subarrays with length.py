t = int(input())

for i in range(t):

    n = int(input())

    arr = list(map(int, input().split()))

    sub = []

    for i in range(n):
        slice = i
        for j in range(i, n):
            temp = arr[i:slice + 1]
            sub.append(temp)
            slice += 1

        # print(sub)

    count = 0
    for i in sub:

        if len(i) in i:
            count += 1

    print(count)

