# cook your dish here

n = int(input())

for i in range(n):
    arr = list(map(int, input().split(' ')))

    myarr = [0] * 4


    # arr.sort()
    #
    # Max = max(arr)
    # count = 0
    #
    # myarr = []
    #
    # for j in range(1, Max + 1):
    #     if Max % j == 0:
    #         myarr.append((j, Max // j))
    #
    # for j in myarr:
    #     lis = []
    #
    #     lis.append(j[0] * j[1])
    #     lis.append(j[0] // j[1])
    #     lis.append(j[0] + j[1])
    #     lis.append(j[0] - j[1])
    #
    #     lis.sort()

    #     if arr == lis:
    #         print(j[0], j[1])
    #         count += 1
    #         break
    # if count == 0:
    #     print(-1, -1)
