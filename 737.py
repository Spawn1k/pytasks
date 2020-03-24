st1 = input()
st2 = input()
st2 = st2[::-1]
razn = 0
for i in reversed(range(len(st2))):
    for j in range(len(st2)):
        if j < i:
            pos = st1.find(st2[j:i])
        if pos != -1:
            if razn < i-j:
                razn = i - j
                srez1 = j
                srez2 = i
print(razn)