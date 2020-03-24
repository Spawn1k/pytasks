import sys
n = int(input())
s = 0
pr = 1
indmin = indmax = 0
mas = list(map(int, input().split()))
minimum = maximum = mas[0]
for i in range(n):
    if mas[i] > 0:
        s = s + mas[i]
    if mas[i] < minimum:
        minimum = mas[i]
        indmin = i
    if mas[i] > maximum:
        maximum = mas[i]
        indmax = i
if indmin > indmax:
    indmax, indmin = indmin, indmax
if indmax - indmin == 2:
    print(s, mas[indmin+1])
    sys.exit()
for i in range(indmin+1, indmax):
    pr = pr * mas[i]
print(s, pr)