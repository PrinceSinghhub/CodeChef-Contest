n = int(input())
for _ in range(n):
    inp = int(input())

    if inp <= 100:
        print(inp)
    if inp > 100 and inp <= 1000:
        print(inp - 25)

    if inp > 1000 and inp <= 5000:
        print(inp - 100)

    if inp > 5000:
        print(inp - 500)
