# 구구단
for i in range(1, 10) :
    print("%s X %d = %d" % (4, i, 3*i))

# 서식 : format함수
for i in range(1, 10):
    print("{} {} {}".format(4, i, 3*i))

# 서식 : f-string함수
for i in range(1, 10):
    print(f"{i} X {3} = {3*i}")

# 뒤에 있는 값들의 위치값 10 20 30 10 30
print("{0} {1} {2} {0} {2}".format(10, 20, 30))

# 자릿수 10칸을 차지하고 공백을 앞에 붙인다 : 오른쪽 정렬
print("{:>10}**".format(5))

# 앞에서부터 숫자를 출력 10칸을 확보 : 왼쪽 정렬
print("{:<10}**".format(5))

# 가운데 정렬
print("{:^10}**".format(5))

# 소수점 이하 자릿수
# 소수점 이하 2자릿수만 출력
print("{:.3}".format(10/3))

# 3자리마다 쉼표
print("{:,}".format(1000000000000000000000))

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(0, 26):
    print(s)
    s = s[1:] + s[0]

# 이중 for 문
for i in range(3, 6):
   print()
   for j in range(1, 10):
       print(f"{i} X {j} = {i*j}")