a = list(map(int, input().split()))
s = ''
pr = 1
answ = 0
for i in range(a[0], a[1]+1):
    s = str(i)
    for j in range(len(s)):
        pr *= int(s[j])
    if pr != 0:
        if i % pr == 0:
            answ += 1
    pr = 1
print(answ)