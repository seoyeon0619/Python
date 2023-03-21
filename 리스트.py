words = ["apple", "banana", "pineapple"]
print(words)

# 인덱싱과 슬라이싱 지원
print(words[0])
print(words[1])
print(words[2])
print(words[3])

print(words[:3])        # 0 1 2
print(words[:3:2])      # 0 2
print(words[::-1])      # 역순
print(words[2:])        # 2

words[:2] = ["kiwi", "kiwi"]
print(words)

words[2:4] = ["ptato", "flower"]
print(words)

words.append("rainbow")
words.append("assembly")
print(words)

words.remove("ptato")
print(words)

words.extend(["blue"])
print(words)

print(words.index("blue"))

print(words.index("magenta"))
print(words.count("magenta"))

if words.count("magenta")==0:
    print("magena is not found")
else:
    print(words.index("magena"))

if "magenta" in words : 
    print("magena is not found")
else:
    print(words.index("magena"))