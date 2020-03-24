a = input()
b = a.split()
bull = 0
cow = 0
for i in range(4):
    if b[0][i] == b[1][i]:
        bull += 1
    else:
        for j in range(3):
            if b[0][i] == b[1][j]:
                cow += 1
print(bull, cow)
            
    