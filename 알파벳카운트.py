s = input("문장 : ")
count = list()
for i in range(0, 26):
    count.append(0)

for i in range(0, len(s)):
    if ord(s[i])>=ord('A') and ord(s[i])<='Z':
        count[ord(s[i]) - ord('A')] +=1
    if ord(s[i])