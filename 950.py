s = input()
sch = 0
i = 0
k = 'abcdefghijklmnopqrstuvwxyz'
answ = ''
while i < len(s):
    while s[i] == '0':
        i += 1
        sch += 1
    answ += k[sch]
    i += 1
    sch = 0
print(answ)