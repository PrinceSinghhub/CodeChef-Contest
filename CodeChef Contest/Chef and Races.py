# cook your dish here
t = int(input())
for i in range(t):

    X, Y, A, B = map(int, input().split())

    pp = [X, Y]
    np = [A, B]

    if np[0] in pp and np[1] in pp:
        print(0)
    elif np[0] in pp or np[1] in pp:
        print(1)
    else:
        print(2)

    # if (X >= 1 and X <= 4 )and (Y >= 1 and Y <= 4 )and( A >= 1 and A <= 4) and (B >= 1 and B <= 4):

    #     if len(set(pp)) == 1 or len(set(np)) == 1 :
    #         print(0)

    #     if sum(pp) == sum(np):
    #         print(0)

    #     else:
    #         count = 0
    #         for i in pp:

    #             if i in np:
    #                 continue
    #             else:
    #                 count += 1
    #         print(count)
    # else:
    #     print(0)