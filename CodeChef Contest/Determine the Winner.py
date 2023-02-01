t = int(input())

for i in range(t):
    a1, a2, b1, b2 = map(int, input().split())

    TMax1 = max(a1, a2)
    TMax2 = max(b1, b2)

    if TMax1 == TMax2:
        print('TIE')

    elif TMax1 < TMax2:
        print('P')

    else:
        print('Q')


