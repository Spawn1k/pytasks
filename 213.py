num = int(input())
s = list(map(int, input().split()))
maximum = sum(s)
prize = int(input())
tries = int(input())
ball = 0
shtraf = 0
thismax = 0
answ = []
k = ''
for i in range(tries):
    point = 0
    mas = list(map(int, input().split()))
    for j in range(len(mas)):
        if mas[j] == 1:
            point += s[j]
    if point == maximum:
        point += prize
    point -= shtraf
    if point > thismax:
        thismax = point
    shtraf += 2
    answ.append(str(thismax))
k = '\n'.join(answ)
print(k)