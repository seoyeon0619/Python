class TestClass:
    # 변수앞에 __(언더바2개) 붙이면 private 변수
    __insCount=0

    # TestClass 객체가 몇 개 만들었는지 확인
    def __init__(self) :
        TestClass.__insCount += 1   
        # self가 아니고 클래스 멤버이므로
        # 객체가 생성될 때마다 __insCount 변수값이 증가
    
    # insCount 값을 출력하는 함수 생성
    # 이 메서드는 static 메서드
    # 매개변수에 self 사용 불가
    # 객체에 속한 함수가 아니라서 객체를 뜻하는 self를 사용하지 않음
    def staticPrintCount():
        print("현재 카운트 {}".format(TestClass.__insCount))
    
    # 별도로 static메서드로 만들어주는 작업 필요
    SPrintCount = staticmethod(staticPrintCount)

    # 자바의 어노테이션처럼 생겼지만, 파이썬에서는 데코레이터라고 부름
    @staticmethod
    def staticPrintCount2():
        print("현재 카운트 {}".format(TestClass.__insCount))

    # 클래스메서드
    # 매개변수로 클래스를 전달
    @classmethod
    def staticPrintCount(cls):
        print("현재 카운트 {}".format(cls.__insCount))
        
# 두 가지 방법 모두 호출 가능
t1 = TestClass()
TestClass.staticPrintCount()
TestClass.SPrintCount()

t2 = TestClass()
TestClass.staticPrintCount()
TestClass.SPrintCount()

# print(t1.__insCount)      -> 볼 수 없음