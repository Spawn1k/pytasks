n = int(input())
fr = []
al = []
mu = []
for i in range(n):
    fr.append(input())
m = int(input())
for i in range(m):
    s = input()
    if s not in fr:
        al.append(s)
    else:
        mu.append(s)
fr.sort()
mu.sort()
al.sort()
friend = ', '.join(fr)
mutfr = ', '.join(mu)
alsofr = ', '.join(al)
print('Friends:', friend)
print('Mutual Friends:', mutfr)
print('Also Friend of:', alsofr)