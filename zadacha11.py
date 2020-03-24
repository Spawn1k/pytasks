a = int(input())
c = list()
d = list()
four = 0
three = 0
b = list(map(int, input().split()))
for i in range(a):
    if b[i] % 2 == 0:
        four += 1
        c.append(b[i])
    else:
        three += 1
        d.append(b[i])
print(*d)
print(*c)
if four >= three:
    print('YES')
else:
    print('NO')

