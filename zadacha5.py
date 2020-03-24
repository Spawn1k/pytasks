import sys
a = input()
b = int(a)
i = 0
min_ = 10
sum_ = 0
c = ''
s = ''
if b == 0:
    print(10)
if b == 1:
    print(1)
    sys.exit()
while b > 1:
    for i in reversed(range(2,10)):
        if b % i == 0:
            c += str(i)
            b /= i
            err = 0
            break
    if (c == '') or (err == -1):
        print(-1)
        sys.exit()
    err = -1
min_ = 10
k = list(c)
if (b == 1):
    for i in range(len(c)):
        min_ = 10
        for j in range(i,len(c)):
            if int(k[j]) < min_:
                min_ = int(k[j])
                index = j
        tmp = k[i]
        k[i] = k[index]
        k[index] = tmp
    print(*k,sep = '')