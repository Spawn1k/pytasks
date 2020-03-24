import math
n = int(input())
por = list(map(int, input().split()))
news = input()
answ = [''] * n
s = ''
for i in range(len(news)):
    if news[i] != ' ':
        s += news[i]
rez = len(s) % n
if rez != 0:
    for i in range(n-rez):
        s += '/'
k = ''
f = 0
fin = ''
for i in range(len(s)):
    f += 1
    k += s[i]
    if f % int(len(s)/n) == 0:
        k += ' '
        f = 0
l = list(k.split())
for i in range(n):
    answ[por[i]-1] = l[i]
for j in range(len(answ[0])):
    for i in range(len(answ)):
            fin += answ[i][j]
for i in range(len(fin)):
    if fin[i] != '/':
        print(fin[i], sep = '', end = '')