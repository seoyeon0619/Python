# 클래스 선언 : 파이썬은 객체를 만들지 않아도 클래스 멤버
class Person:
    name = "홍길동"
    age = 23

    def output(self):    # 첫 번째 매개변수로 self 
                         # 객체변수나 함수 사용 시 반드시 self로 호출
        print("이름 : ", self.name)
        print("나이 : ", self.age)

p1 = Person()            # 인스턴스(객체) 생성
p1.output
