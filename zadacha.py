a=input()
c = 0
s = 0
for i in range(len(a)):
    if a[i] == '0':
        c += 1
        if c > s:
            s = c
    if a[i] == '1':
        c = 0
print(s)
