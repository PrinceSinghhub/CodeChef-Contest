t = int(input())
for i in range(t):

    n = int(input())
    Bin = input()

    Mid = n // 2

    count = 0

    if Bin == Bin[::-1]:
        print(0)


    else:
        for i in range(Mid):

            if Bin[i] != Bin[n - i - 1]:
                count += 1
                # print(count)
        print((count + 1) // 2)