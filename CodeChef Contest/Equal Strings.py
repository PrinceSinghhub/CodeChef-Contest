t = int(input())
for _ in range(t):

    n = int(input())
    A = input()
    B = input()

    ans = ''
    mystr = ''

    for i in range(len(A)):
        if A[i] != B[i]:
            ans += A[i]
            mystr += B[i]

        else:
            pass
    print(len(''.join(set(mystr))))