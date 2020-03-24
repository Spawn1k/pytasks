s = input()
answ = ''
mass = [int(i) for i in range(27)]
sym = 'abcdefghijklmnopqrstuvwxyz'
l = []
for i in range(len(s)):
    k = sym.find(s[i])
    l.append(mass[k])
l.sort()
for i in range(len(l)):
    answ += sym[l[i]]
print(answ)