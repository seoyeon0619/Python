"""
while 조건식:
    코드
"""

i = 1
while i<=10:
    print(i)
    i = i + 1

# 정수를 입력받아 합계와 평균 구하기
# 음수 입력 시 끝냄

dataList=[]
num = int(input("정수 : "))
while num>=0:
    dataList.append(num)
    num = int(input("정수 : "))

print(sum(dataList))    
print(sum(dataList)/len(dataList))

