# cook your dish here
t = int(input())

for i in range(t):

    n = int(input())

    arr = list(map(int, input().split()))

    flag = True
    for i in range(n - 1):

        if arr[i] <= arr[i + 1]:
            continue
        else:
            print('No')
            flag = False
            break

    if flag == True:
        print("Yes")

