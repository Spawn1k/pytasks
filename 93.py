n = int(input())
bog = []
c = 0
ind = 0
answ = []
for i in range(n):
    answ.append(c)
for i in range(n):
    tmp = input()
    bog.append(tmp)
m = int(input())
for i in range(m):
    tmp = input()
    for j in range(n):
        if len(tmp) == len(bog[j]):
            while ind < len(tmp):
                if tmp[ind] != bog[j][ind]:
                    c += 1
                ind += 1
            if c == 1:
                answ[j] += 1
        ind = 0
        c = 0
print(*answ)