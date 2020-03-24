n = int(input())
sch = 0
count = []
for i in range(2, n*2):
    err = 0
    if i > 10 and i % 5 == 0:
        continue
    for j in count:
        print(j, ' ', i, ' ', count)
        if j*j > i:
            break
        if i % j == 0:
            err = 1
            break
    if err == 0:
        count.append(i)
for i in range(len(count)):
    if count[i] > n:
        sch += 1
print(sch)