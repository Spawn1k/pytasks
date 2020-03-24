def num(char):
    string = 'ABCDEFGH'
    return string.find(char)
summa = 0
a = [[0] * 8 for i in range(8)]
figures = list(input().split())
stolb = num(figures[0][0])
strok = int(figures[0][1]) - 1
a[strok][stolb] += 100
for i in range(len(a)):
    a[strok][i] += 1
    a[i][stolb] += 1
tmpstolb = stolb
tmpstrok = strok
while strok < 8 and stolb < 8:
    a[strok][stolb] += 1
    stolb += 1
    strok += 1

strok = tmpstrok
stolb = tmpstolb
while strok < 8 and stolb >= 0:
    a[strok][stolb] += 1
    stolb -= 1
    strok += 1
strok = tmpstrok
stolb = tmpstolb
while strok >= 0 and stolb < 8:
    a[strok][stolb] += 1
    stolb += 1
    strok -= 1
strok = tmpstrok
stolb = tmpstolb
while strok >= 0 and stolb >= 0:
    a[strok][stolb] += 1
    stolb -= 1
    strok -= 1
stolb = num(figures[1][0])
strok = int(figures[1][1]) - 1
a[strok][stolb] += 100
for i in range(len(a)):
    a[strok][i] += 1
    a[i][stolb] += 1
    
stolb = num(figures[2][0])
strok = int(figures[2][1]) - 1
a[strok][stolb] += 100
tmpstrok = strok
tmpstolb = stolb
strok += 2
stolb += 1
for i in range(8):
    strok = tmpstrok
    stolb = tmpstolb
    if i == 0:
        strok += 2
        stolb += 1
        if strok <= 7 and stolb <= 7:
            a[strok][stolb] += 1
    if i == 1:
        strok += 1
        stolb += 2
        if strok <= 7 and stolb <= 7:
            a[strok][stolb] += 1
    if i == 2:
        strok -= 1
        stolb += 2
        if strok >= 0 and stolb <= 7:
            a[strok][stolb] += 1
    if i == 3:
        strok -= 2
        stolb += 1
        if strok >= 0 and stolb <= 7:
            a[strok][stolb] += 1
    if i == 4:
        strok -= 2
        stolb -= 1
        if strok >= 0 and stolb >= 0:
            a[strok][stolb] += 1      
    if i == 5:
        strok -= 1
        stolb -= 2
        if strok >= 0 and stolb >= 0:
            a[strok][stolb] += 1
    if i == 6:
        strok += 1
        stolb -= 2
        if strok <= 7 and stolb >= 0:
            a[strok][stolb] += 1     
    if i == 7:
        strok += 2
        stolb -= 1
        if strok <= 7 and stolb >= 0:
            a[strok][stolb] += 1         
for i in range(len(a)):
    for j in range(len(a[i])):
        if 0 < a[i][j] < 100:
            summa += 1
print(summa)