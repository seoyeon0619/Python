# iterator 또는 Enumeration 
# 현재 객체 지향언어에 있는 개념
# 클래스를 만드는데 클래스가 컬랙션류일 때
# 내부에 배열을 갖거나 linkedlist 등의 무엇인가를 담아두어야 하는 클래스를 설계할 때  
# 외부의 클래스 사용자가 클래스 내부의 실제 데이터 배치상태를 몰라도
# 언제나 동일한 형태로 전체 데이터를 순회할 수 있도록 하는 인터페이스를 말함
# 배열의 경우에는 a[0], a[1], ... 내부에 링크드 리스트의 경우
# a, a.next, a.next.next, ... 이런 식으로 실제 데이텅 대한 접근 방법은 다름
# 그래서 고민해낸 것이 iterator 나 Enumeration 
# 맨 처음부터 차례 차례 다음 데이터로 이동하는 것을 보장
# for 변수명 in iterable 객체

for i in [1,2,3,4,5,6,7,8,9,10] :
    print(i)

# range(시작값,종료,증감치) - iterable
print(range(1,11,1))


for i in range(1, 101, 1) :
    if i%10 == 0 :
        print(i, end="\n")
    else :
        print(i, end="   ")

k=1
for i in range(0, 10) :
    for j in range(0, 10):
        print(k, end=" ")
        k = k+1
    print()

print(ord("A"))
# 키보드로 문장을 입력받아서 문장안에 쓰인 문자의 개수를 세서 출력
words = input("입력 : ")
print(words)

