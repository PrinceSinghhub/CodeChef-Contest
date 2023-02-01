t = int(input())

for i in range(t):

    n,k = map(int,input().split())

    if k == 2:
        print('OOD')

    elif k == 1:
        if n % 2 == 0:
            print('EVEN')
        else:
            print('OOD')

    else:
        if k % 2 == 0:
            print('EVEN')

        else:
            k-=1
            if k % 2 == 0:
                print('EVEN')



            else:
                print("OOD")
