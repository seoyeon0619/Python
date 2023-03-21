# dict type : dictionary의 약자
# 자바의 HashMap과 유사
# 인덱싱, 슬라이싱 불가
# 키와 값 쌍의 형태로 저장

mydic = {"red" : "빨강", "green" : "초록", "blue" : "파랑"}
print(mydic)
print(mydic["red"])
print(mydic.green)

mydic["black"]="검정"
print(mydic)

mydic["red"]="빨강"
print(mydic)

del mydic["red"]
print(mydic)
