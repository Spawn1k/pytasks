import sys
s = input()
s = s.lower()
word = [0 for i in range(27)]
corr = 'abcdefghijklmnopqrstuvwxyz'
sym = s.find(' ')
for i in range(sym):
    if s[i] == s[sym+1+i]:
        print('NO')
        sys.exit()
for i in range(sym):
    k = corr.find(s[i])
    word[k] += 1
for i in range(sym+1, len(s)):
    k = corr.find(s[i])
    word[k] -= 1
i = 0
while word[i] == 0 and i < 26:
    i += 1
if i == 26:
    print('YES')
else:
    print('NO')