def add(x, y):
    return x+y

print(add(1,2))

x=10
y=10
print(add(x, y))

# 함수의 주소를 다른 변수에 저장
calc = add
print(calc(11,12)) # java는 인터페이스로 처리 

# 1~limit 까지의 합계를 구하여 반환하는 함수
def sigma(limit):
    if limit<1:     # 함수를 sigma(0)으로 호출하면 0이 limit보다 작으므로 None 반환 후 종료 
        return      # 값을 보내지 않을 경우 None 반환
    
    s = 0
    for i in range(1, limit+1):
        s += i
    return s

print(sigma(0))
print(sigma(10))

def isZero(args1):
    return args1==0 # 연산 수행 결과를 반환
print(isZero(6))
print(isZero(0))

# 매개변수로 전달 시 값이 변경가능한 경우
# 리스트나 딕셔너리 형태
def changeValue(a):
    a = a * 10

x = 11      #x가 생성되는 영역과 a가 생성되는 영역은 서로 다르다
            # 함수가 호출될 때 x 변수에 저장된 값이 a변수로 복사된다
            # a변수 값을 바꾸어도 x변수와 a 변수는 서로 다른 메모리 공간을 차지하므로
            # 서로 영향을 미치지 않는다
x = changeValue(x)
print("x = ", x)

a = [0,0,0,0,0]
def setValue(aa ):
    for i in range(0, len(aa)):
        aa[i] = i+1
setValue(a) # list타입이 전달되면 list타입은 값을 바꿔서 온다
print(a)

def setDictValue(colors):
    colors["red"]="빨강"
    colors["blue"]="파랑"
    colors["green"]="초록"
out_colors={} # dict객체 생성
setDictValue(out_colors)
print(out_colors)

