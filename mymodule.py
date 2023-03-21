def sigma(limit=10):
    s=0

    # limit + 1 : range가 마지막 숫자를 포함하지 않기 때문
    for i in range(1, limit+1):
        s = s + i
    return s

def circle(radius=5):
    return radius*radius*3.14

def toUpper(s):
    # chr(코드) -> 문자
    # ord(문자) -> 코드
    temp = ""
    for c in s:
        if(ord(c) >= ord('a') and ord(c) <= ord('z')):
            temp = temp + chr(ord(c)-32)
        else:
            temp = temp + c
    return temp

# 내가 main으로 사용할 수도 있고, 다른 모듈에서 import되어 사용될 수 도 있음
if __name__ == "__main__":  # 내장변수 : main으로 사용 시, __main__이라는 이름이 옴
    print(sigma(100))       # module로 사용 시, 파일명이 옴
    print(circle(5))
    print(toUpper("I like star"))
