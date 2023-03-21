# 1. 텍스트 파일 읽기
f = open("text.txt", "r", encoding="utf-8")

# open("파일명", "모드", 인코딩) : text.txt 파일을 읽기 모드로 연다
# 한글의 경우 반드시 인코딩
# f는 읽기윟 ㅐ연 파일에 대한 참조를 가지고 있음

lines = f.readlines()                # 파일을 한번에 다 읽음
for line in lines:
    # korea\n   [0:len('korea') - 1]
    line = line[:len(line) - 1]     # 맨 뒤에 엔터키 지움
    print(line)
f.close()

# with 문법 : 자원을 사용하고 자동 반납해주는 구문
with open("text.txt", "r", encoding="utf-8") as f:
    lines = f.readlines
    for line in lines:
        line = line[:len(line) - 1]     # 맨 뒤에 엔터키 지움
        print(line)

# 한 줄 씩 읽어서 처리
with open("text.txt", "r", encoding="utf-8") as fin:
    line = fin.readline()
    while line != "" :
        print(line[0:len(line) - 1])
        line = fin.readline()