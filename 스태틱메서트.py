class MyType:
    @staticmethod
    def isCapital(s):
        for c in s:
            if(ord(c) < ord('A') or ord(c) > ord('Z')):
                return False
        return True     
    # for문을 모두 수행해도 return이 안된 경우는 모두 대문자
    # True 반환

    @staticmethod
    def isNumeric(s):
        for c in s:
            if(ord(c) < ord('0') or ord(c) > ord('9')):
                return False
        return True 

# 객체를 만들지 않고도 사용 가능
# 주로 데이터가 공유될 필요가 없는데 기능상 묶이는 게 맞을 경우에 사용
# Math클래스 (수학함수)    

print(MyType.isCapital("TEST"))
print(MyType.isCapital("Test"))
print(MyType.isCapital("tEst"))

print(MyType.isCapital("123"))
print(MyType.isCapital("T123"))