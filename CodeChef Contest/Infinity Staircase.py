t = int(input())
for i in range(t):
    x = int(input())
    if (x == 1):
        print("0")
    elif (x == 2 or x == 3):
        print("1")
    elif (x % 5 == 0 or x % 5 == 1):
        print(int((x // 5) * 2))


    else:
        print(int(x // 5) * 2 + 1)
