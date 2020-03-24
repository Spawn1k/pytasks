import sys
p = input()
if p[0].isupper():
    print('Error!')
    sys.exit()
nach = 0
mem = 10
k = 0
s = ''
c = []
ind = p.find('_')
if ind == 0:
    print('Error!')
    sys.exit()
if p.islower() and ind == -1:
    print(p)
    sys.exit()
if ind != -1:
    for i in range(len(p)):
        if p[i].isupper():
            print('Error!')
            sys.exit()
    while ind != -1:
        ind = p.find('_', ind)
        if ind != -1 and ind != 0:
            if p[ind+1:ind+2].isupper() or ind == len(p)-1 or ind == mem+1:
               print('Error!')
               sys.exit()
            else:
                s += p[nach:ind] + p[ind+1:ind+2].upper()
                nach = ind+2
            if ind != 0:
                mem = ind
            ind += 1
        else:
            s += p[nach::] 
    print(s)
else:
    for i in range(len(p)):
        if p[i].isupper():
            c.append(i)
            k += 1
    for i in range(k):
        s += p[nach:c[i]] + '_' + p[c[i]:c[i]+1].lower()
        nach = c[i] + 1
    s += p[nach::]
    print(s)