def isunique(string):
    letters = letter
    for i in range(len(string)):
        if string[i] in letters:
            letters.remove(string[i])
        else:
            return False
    return True
    
a = int(input())
newstr = ''
mas = []
answ = []
masq = ''
masq2 = ''
err = 1
main = 'the quick brown fox jumps over the lazy dog'
for i in range(len(main)):
    if main[i] != ' ':
        masq += '1'
    else:
        masq += ' '
for i in range(a):
    s = input()
    mas.append(s)
    if len(s) == len(main):
        masq2 = ''
        for j in range(len(s)):
            if s[j] != ' ':
                masq2 += '1'
            else:
                masq2 += ' '
        if masq == masq2:
            newstr = ''
            for j in range(len(s)):
                t = s.find(s[j])
                newstr += main[t]            
            if newstr == main:
                shifr = s
                err = -1
if err == -1:
    for i in mas:
        newstr = ''
        for j in range(len(i)):
            t = shifr.find(i[j])
            newstr += main[t]
        answ.append(newstr)
    newstr = '\n'.join(answ)
    print(newstr)
else:
    print('No solution')