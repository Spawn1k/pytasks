s = list(map(int, input().split()))
black = 0
green = 0
blue = 0
red = 0
for i in range(1, s[0]+1):
    for j in range(1, s[1]+1):
        if (i*j) % 5 == 0:
            blue += 1
        elif (i*j) % 3 == 0:
            green += 1        
        elif (i*j) % 2 == 0:
            red += 1
        else:
            black += 1
print('RED : ', red,'\nGREEN : ', green, '\nBLUE : ', blue, '\nBLACK : ', black,
      sep = '')