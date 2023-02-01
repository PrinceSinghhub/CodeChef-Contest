t = int(input())
for _ in range(t):

    normi_burg, premi_burg , num_burg, budget = map(int, input().split())

    if budget / premi_burg >= num_burg:
        print(0," ", num_burg)
    elif budget / normi_burg < num_burg:
        print(-1)
    else:

        g = int(premi_burg * num_burg)
        h = int(normi_burg - premi_burg)
        i = int((budget - g) / h)

        if (budget - g) % h != 0:
            i+=1

        print(i,' ', num_burg - i)
