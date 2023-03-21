# 튜플은 리스트와 유사하다
# 리스트는 데이터 읽고 쓰기 가능
# 튜플은 읽기만 가능

a, b = 5, 6
print("a = ", a)
print("b = ", b)

a = (1,2,3,4,5)
print(a, type(a))

for i in a:
    print(i)

print(a[0:3])

# 함수만들기
def add(x, y):
    # 이때 매개체가 되는 변수들은 외부의 값을 읽어오고나서 외부변수와의 연결은 종료
    x = x*2
    y = y*2

    # 원래는 함수 값을 하나만 반환해야 함
    # 하나만 반환해야 하므로 두개를 묶어 튜플로 묶어서 보냄
    return x, y

x=1
y=7

print(type(add(x,y)))

x, y = add(x, y)
# 함수 수행 후 결과는 튜플로 반환
# 별도의 변수에 tuple값을 하나씩 할당
print("x = ", x)
print("y = ", y)