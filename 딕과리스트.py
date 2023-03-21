score = {
    "name":["홍길동", "임꺽정", "장길산", "조승연"],
    "kor":[90, 80, 90, 100],
    "eng":[90, 80, 90, 100],
    "mat":[90, 80, 90, 100]
    }

print(score["name"][0])
print(score["name"][1])
print(score["name"][2])
print(score["name"][3])

print(score["kor"][0])
print(score["eng"][1])
print(score["mat"])

score["total"] = list()

score["total"].append(score["kor"][0] + score["eng"][0] + score["mat"][0])
score["total"].append(score["kor"][1] + score["eng"][1] + score["mat"][1])
score["total"].append(score["kor"][2] + score["eng"][2] + score["mat"][2])
score["total"].append(score["kor"][3] + score["eng"][3] + score["mat"][3])

print(score["total"])
print(score)

score = [
    {"name" : "홍길동", "kor":90, "eng":80, "mat":100},
    {"name" : "임꺽정", "kor":90, "eng":80, "mat":100},
    {"name" : "장길산", "kor":90, "eng":80, "mat":100},
    {"name" : "조승연", "kor":90, "eng":80, "mat":100},
    {"name" : "강호동", "kor":90, "eng":80, "mat":100},
    {"name" : "유재석", "kor":90, "eng":80, "mat":100}
]

print(score[0]["name"], score[0]["kor"], score[0]["eng"], score[0]["mat"])

for i in range(0, len(score)):
    print(score[i]["name"], score[i]["kor"], score[i]["eng"], score[i]["mat"])

for s in score:
    print(s["name"], s["kor"], s["eng"], s["mat"])
