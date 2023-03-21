with open("test2.txt", "w", encoding="utf-8") as fout:
    line = input("아무거나")
    while line != "" :
        print(line, file = fout)    # 출력이 파일로 감
        line = input("아무거나")

with open("test2.txt", "r", encoding="utf-8") as fin:
    lines = fin.readlines()
    print(lines)

