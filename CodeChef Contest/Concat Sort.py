for _ in range(int(input())):

    n = int(input())

    arr = list(map(int,input().split()))[:n]
    arr2 = sorted(arr)
    arr3 = [arr.index(arr2[0]),0]
    null_arr = [0]*n

    for i in range(2):
        arr3[0] = 0
        while arr3[0] < n:
            if not null_arr[arr3[0]] and arr[arr3[0]] == arr2[arr3[1]]:
                null_arr[arr3[0]] = 1
                arr3[0]+=1
                arr3[1]+=1
            else:
                arr3[0]+=1

    if arr3[0] == arr3[1]:
        print('YES')
    else:
        print('NO')
