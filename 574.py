s1 = input()
s2 = input()
word = [0 for i in range(27)]
corr = 'abcdefghijklmnopqrstuvwxyz'
corr = corr.upper()
for i in range(len(s1)):
    k = corr.find(s1[i])
    word[k] += 1
for i in range(len(s2)):
    k = corr.find(s2[i])
    word[k] -= 1
i = 0
while word[i] == 0 and i < 26:
    i += 1
if i == 26:
    print('YES')
else:
    print('NO')