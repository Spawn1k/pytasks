a = list(map(int, input().split()))
c = list()
d = list()
err = 0
while a[0] > 1:
    for i in range(2,10):
        if a[0] % i == 0:
            c.append(i)
            a[0] /= i
            err = 0
            break
    if err == -1:
        c.append(a[0])
        break   
    err = -1
while a[1] > 1:
    for i in range(2,10):
        if a[1] % i == 0:
            d.append(i)
            a[1] /= i
            err = 0
            break
    if err == -1:
        d.append(a[1])
        break   
    err = -1
print(c)
print(d)