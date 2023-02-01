n = int(input())
for _ in range(n):

    A, B = map(int, input().split())

    if A == B:
        print('YES')


    else:
        if A > B:
            while B < A:
                B *= 2
        if B > A:
            while A < B:
                A *= 2

        if A == B:
            print("YES")
        else:
            print("NO")
