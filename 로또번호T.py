import random
class MyLotto:
    def __init__(self):
        self.lottoList = list()

    def createLotto(self):

        while True:
            num = random.randint(1, 10)
            if num not in self.lottoList:       # 중복배제
                self.lottoList.append(num)
            if len(self.lottoList) == 6:
                break
    
    def display(self):
        print(self.lottoList)

m1 = MyLotto()
m1.createLotto()
m1.display()