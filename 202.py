s = input()
st = input()
ind = 0
answ = []
i = 0
while i != -1:
    i = s.find(st, i)
    answ.append(i)
    if i != -1:
        i += 1
print(*answ[:-1])