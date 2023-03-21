scoreList = []      # 전역개체

def isNumeric(s):   # 숫자로만 이루어진 문자열이면 True반환
    for i in range(0, len(s)):
        if ord(s[i]) < ord('0') or ord(s[i]) > ord('9') :
            return False
    return True     # False 마지막까지 왔다 -> 숫자로만 구성

def getNumber(subject):
    temp = input(subject+" : ")
    while not isNumeric(temp) :
        print("숫자를 입력하세요")
        temp = input(subject+" : ")
    return int(temp)

def getScore(subject) :
    temp = getNumber(subject)
    while temp < 0 or temp > 100 :
        print("0에서 100까지의 값만 입력할 수 있습니다")
        temp = getNumber(subject)
    return temp    

def append():
    score = {}      # 자바도 Dto안만들고 Map 사용
                    # 파이썬의 dict타입이 자바의 HashMap과 유사
    score["name"] = input("이름 : ")
    score["kor"] = getScore("국어 : ")
    score["eng"] = getScore("영어 : ")
    score["mat"] = getScore("수학 : ")
    scoreList.append(score)
    score["sum"] = score["kor"] + score["eng"] + score["mat"]
    score["avg"] = score["sum"]/len(score)

def output():
    for score in scoreList :
        print("{} {} {} {} {} {}".format(score["name"], score["kor"], score["eng"], score["mat"], score["sum"], score["avg"]))


def start() :
    while True :
        print("1. 추가")
        print("2. 출력")
        sel = input("선택 : ")

        if sel == "1" :
            append()
        elif sel == "2" :
            output()
        elif sel == "0" :
            return
        
start()