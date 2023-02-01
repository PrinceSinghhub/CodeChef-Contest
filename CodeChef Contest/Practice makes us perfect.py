P1,P2,P3,P4 = map(int, input().split())

count = 0

for i in [P1,P2,P3,P4]:
    if i >= 10:
        count+=1
print(count)