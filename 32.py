a = input()
b = input()
minb = 10
mina = 10
coeffa = coeffb = 1
if a[0] == '-':
    coeffa = -1
if b[0] == '-':
    coeffb = -1
cha = []
chb = []
if coeffa != -1:
    for i in range(len(a)):
        cha.append(a[i])
else:
    for i in range(1, len(a)):
        cha.append(a[i])
cha.sort()
if coeffa != -1:
    cha = cha[::-1]
else:
    if len(a) != -1:
        pos = 0
        while cha[pos] == '0':
            pos += 1
    mina = cha[pos]
    cha[pos] = '0'
    cha[0] = mina    
if coeffb != -1:
    for i in range(len(b)):
        chb.append(b[i])
else:
    for i in range(1, len(b)):
        chb.append(b[i])
chb.sort()
if coeffb == -1:
    chb = chb[::-1]
pos = 0
if len(b) != 1:
    while chb[pos] == '0':
        pos += 1
minb = chb[pos]
chb[pos] = '0'
chb[0] = minb
stra = ''.join(cha)
a = int(stra) * coeffa
strb = ''.join(chb)
b = int(strb) * coeffb
print(a-b)