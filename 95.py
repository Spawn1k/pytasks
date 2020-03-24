s = input()
ch = 0
summ = 0
st = s
while len(st) > 1:
    for i in range(len(st)):
        summ += int(st[i])
    st = str(summ)
    ch += 1
    summ = 0
print(st, ch)