# 생성자를 통해서 변수 선언
class ScoreData :
    def __init__(self, name="", kor=0, eng=0, mat=0):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.process()

    # 총 점, 평균 
    def process(self):
        self.total = self.kor + self.eng + self.mat
        self.avg = self.total/3
        if self.avg >= 90:
            self.grade = "수"
        elif self.avg >= 80:
            self.grade = "우"
        elif self.avg >= 70:
            self.grade = "미"
        elif self.avg >= 60:
            self.grade = "양"
        else:
            self.grade = "가"
            
    def display(self):
        print(self.name, self.kor, self.eng, self.mat,
              self.total, self.avg, self.grade)