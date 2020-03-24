s = input()
news = s[2::]
newmax = int(news)
for i in range(len(s)):
    for j in range(i+1, len(s)):
        news = s[0:i]
        news += s[i+1:j] + s[j+1::]
        if int(news) > newmax:
            newmax = int(news)
print(newmax)