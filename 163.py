s = input()
if s[1] == '+':
    state = 1
else:
    state = 2
k = s.find('x')
if k == 0:
    if state == 1:
        print(int(s[4]) - int(s[2]))
    else:
        print(int(s[4]) + int(s[2]))
if k == 2:
    if state == 1:
        print(int(s[4]) - int(s[0]))
    else:
        print(int(s[0]) - int(s[4]))
if k == 4:
    if state == 1:
        print(int(s[0]) + int(s[2]))
    else:
        print(int(s[0]) - int(s[2]))