from ScoreData import ScoreData
import pickle

class ScoreManager:
    dataList = list()
    
    def __init__(self):
        self.dataList.append(ScoreData("A", 100,100,100))
        self.dataList.append(ScoreData("B", 90,90,90))
        self.dataList.append(ScoreData("C", 80,80,80))
        self.dataList.append(ScoreData("D", 70,70,70))
        self.dataList.append(ScoreData("E", 60,60,60))
        self.dataList.append(ScoreData("F", 50,50,50))

    def append(self):
        s = ScoreData()
        s.name = input("이름 : ")
        s.kor = int(input("국어 : "))
        s.eng = int(input("영어 : "))
        s.mat = int(input("수학 : "))
        s.process()
        self.dataList.append(s)

    def output(self):
        for item in self.dataList:
            item.display()

    def search(self):
        name = input("이름 검색 : ")
        # filter(람다식, 리스트)
        # filter 함수에 전달 할 람다식은 반환값이 True/False
        # filter에 전달되는 람다함수는 데이터 요소마다 호출됨
        # 데이터 요소를 파라미터로, 반환값은 True/False
        find = False
        for i in filter(lambda x : x.name == name, self.dataList):
            i.display()
            find = True
        if find == False:
            print("존재하지 않는 이름입니다.")

    def modify(self):
        name = input("이름 검색 : ")
        modifyList = list(filter(lambda x : x.name == name, self.dataList))
        if len(modifyList) == "0" : 
            print("존재하지 않는 이름입니다.")
            return
        
        i = 1
        for item in modifyList :
            print("{} 번째".format(i))
            item.display()

        pos = int(input("수정할 항목의 번호를 입력하세요"))
        if pos <0 or pos> len(modifyList):
            print("잘못 선택하였습니다.")
            return
        
        modifyList[pos - 1].name = (input("이름 : "))
        modifyList[pos - 1].kor = int(input("국어 : "))
        modifyList[pos - 1].eng = int(input("영어 : "))
        modifyList[pos - 1].mat = int(input("수학 : "))
        modifyList[pos - 1].process()
    
        print("수정되었습니다.")

    def delete(self):
        name = input("삭제할 이름 : ")
        deleteList = list(filter(lambda x : x.name == name, self.dataList))
        if len(deleteList) == "0" : 
            print("존재하지 않는 이름입니다.")
            return
        
        i = 1
        for item in deleteList :
            print("{} 번째".format(i))
            item.display()

        pos = int(input("삭제할 항목의 번호를 입력하세요"))
        if pos <0 or pos> len(deleteList):
            print("잘못 선택하였습니다.")
            return
        
        deleteItem = deleteList[pos - 1]
        self.dataList.remove(deleteItem)

        print("삭제되었습니다")
    
    def sort(self):
        sortedList = sorted(self.dataList, key=lambda item : item.grade)

        for item in sortedList:
            item.display()

    def save(self):
        f = open("score.txt", "w", encoding="utf-8")
        for item in self.dataList:
            print("{} {} {} {}".format(item.name, item.kor, item.eng, item.mat), file = f)
            f.close

    def save2(self):
        file = open("score.bin", "wb")      
        pickle.dump(self.dataList, file=file)
        file.close()
    
    def load(self):
        self.dataList = list()      #불러오기 할 때 이전 데이터 삭제해야하기 때문에 새로운 객체생성
        f = open("score.txt", "r", encoding="utf-8")
        line = f.readline()
        while line != "" :
            # 토큰 분리
            tokens = line.split(" ")    # 공백기준으로 토큰 분리
            data = ScoreData()
            data.setName(tokens[0])
            data.setKor(int(tokens[0]))
            data.setEng(int(tokens[0]))
            data.setMat(int(tokens[0]))
            self.dataList.append(data)
            line = f.readline()     # 다음 줄 읽음

    def load2(self):
        file = open("score.bin", "rb")      
        self.dataList = pickle.load(file=file)
        file.close()
            
    def menuDisplay(self):
        print("1. 추가")
        print("2. 출력")
        print("3. 검색")    # filter
        print("4. 수정")    # filter
        print("5. 삭제")    # filter
        print("6. 정렬")    # sorted
        print("7. 저장")
        print("8. 불러오기")
        print("9. pickle로 저장")
        print("10. pickle로 불러오기")
        print("0. 종료")

    def start(self):
        while True:
            self.menuDisplay()
            sel = input("선택 : ")
            if sel == "1" :
                self.append()
            elif sel == "2" :
                self.output()
            elif sel == "3" :
                self.search()
            elif sel == "4" :
                self.modify()
            elif sel == "5" :
                self.delete()
            elif sel == "6" :
                self.sort()
            elif sel == "7" :
                self.save()
            elif sel == "8" :
                self.load()
            elif sel == "9" :
                self.save2()
            elif sel == "10" :
                self.load2()
            elif sel == "0" :
                print("종료 ~,~")
                return
            
if __name__ == "__main__":
    sm = ScoreManager()
    sm.start()
  