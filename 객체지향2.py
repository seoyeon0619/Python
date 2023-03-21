class Person:
    # 변수 선언이 가능한 부분
    # 이곳에 선언된 변수의 소속은 클래스, 객체가 아님
    # 객체를 새로 생성할 때 메모리가 확보되지 않음
    # static을 안써도 알아서 static 상황

    name = "홍길동"     # 변수만 선언하는 방법 없음
                        # 변수에는 반드시 값을 줘야함
    score = list()

    # 생성자는 한 개만 만들 수 있음
    # 지금처럼 생성자를 만들면 매개변수값을 반드시 줘야함
    # 기본생성자 없는 상황이 되었음
    # p1 = Person() 사용불가
    # p1 = Person("홍길동", [100,90,80])
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def append(self, name="", score=[100, 100, 100]):
        self.name = name
        self.score = score
    
    def output(self):
        print(self.name, self.score)

p1 = Person("홍길동", [90, 90, 90])
p2 = Person("임꺽정", [80, 80, 80])

p1.score[0]=1000
p1.output()
p2.output()

# 클래스에 새로운 변수를 추가
Person.phone = "010-9999-9999"

print(p1.name, p1.score, p1.phone)

# 객체에 중간에 새로운 변수 추가할 수 있으나
# 사용하지 말 것
p2.address = "서울"
print(p2.name, p2.score, p2.address)

# 클래스 상속
class Student(Person) : 
    def __init__(self, name="", score=list(), className=""):
        Person.__init__(self, name, score)      # 부모 생성자 호출
        self.className = className
    
    def output(self):
        print(self.name, self.score, self.className)

s1 = Student("학생1", [100,100,100], "1반")

# 파이썬도 최상위 클래스가 object
# 특별히 상속을 받지 않아도 object를 상속받음
print(isinstance(s1, Student))
print(isinstance(s1, Person))
print(isinstance(s1, object))