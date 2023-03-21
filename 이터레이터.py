s = "Hello"

it = iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

a = [1,2,3,4,5]
ait = iter(a)
print(next(ait))
print(next(ait))
print(next(ait))
print(next(ait))
print(next(ait))

def generator():        # 무한 숫자 생성
    i=1
    while True:
        # return i      # 함수 종료
        yield i         # 함수를 호출하면 여기까지의 일을 저장하고 값을 보냄
        i = i+1         # 의미 없는 문장

for i in generator():
    print(i)

def generator2(limit=10):
    i=1
    while i<=limit:
        yield i 
        i = i+1
print("두번째 제너레이터 ~,~")
for i in generator2():
    print(i)

g = generator2()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


