a = int(input())
mas = ['A', 'B', 'C', 'E', 'H', 'K', 'M', 'O',  'P', 
       'T', 'X', 'Y']
output = []
for i in range(a):
    k = 0
    s = input()
    if s[0] in mas:
        if s[1:4].isdigit():
            if s[4] in mas and s[5] in mas:
                k = 1
    if k == 1 and len(s) == 6:
        output.append('Yes')
    else:
        output.append('No')
answ = '\n'.join(output)
print(answ)