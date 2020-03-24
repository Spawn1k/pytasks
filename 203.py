s = input()
p = input()
f = s
prs = p
count = 0
while s != p:
    prs = s[-1::]
    s = s[:-1]
    s = prs + s
    count += 1
    if count == len(s):
        count = -1
        break
print(count)