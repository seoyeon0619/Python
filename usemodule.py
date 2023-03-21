import mymodule

print("모듈 사용하기")

print(mymodule.sigma(100))
print(mymodule.circle(7))
print(mymodule.toUpper("korea"))

# import 구문은 모듈명.함수명() 형태로 사용해야 함
# 마치 내가 가지고 있는 함수처럼 가지고 올 수도 있음
# 모듈명 생략 가능
from mymodule import sigma, circle, toUpper
print(sigma(200))
print(circle(14))
print(toUpper("math"))
