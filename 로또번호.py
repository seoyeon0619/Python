import random

# for i in range(1, 10):
#     print(random.randint(1,3))

# 객체지향으로 중복배제하면서 만들기
def getNumber():
    print("=== 로또 번호 생성 ===")
    lotto = [i for i in range(1, 46)]
    for i in range(6):
        random.shuffle(lotto)
        print(lotto[0:6])

def luckyNumber():
    print("=== 당첨번호 ===")
    luckyNum = [i for i in range(1,46)]
    random.shuffle(luckyNum)
    print(luckyNum[0:6])

def start():   
    getNumber()
    print()
    luckyNumber()

start()