t = int(input())
for _ in range(t):
    N = int(input())
    i = 1
    flag = 0
    while i*i <= N:
        if (N-2*i) % (i+2) == 0 and N != (2 * i):
            print("YES")
            flag = 1
            break
        i += 1
    if flag == 0:
        print("NO")