import pandas as pd

# dict 안에 list 구조
data ={
    "name" : ["홍길동", "장길산", "임꺽정", "김성훈"],
    "kor" : [90, 90, 90, 90],
    "eng" : [90, 90, 90, 90],
    "mat" : [90, 90, 90, 90]
}

df = pd.DataFrame(data)
print(df)

#iloc : indexing을 통해서 접근
print(df.iloc[0,0])

# 필드명으로 접근
print(df.loc[0, "name"])

# 0번째 행
print(df.iloc[0, :])

# 한 행 출력
print(df.loc[0, :])

# 1번째 열
print(df.iloc[:, 0])


# 홍길동, 임꺽정 데이터만 추출
print(df.iloc[[0,2], :])

# 열을 추출 name, eng, mat
print(df.loc[:, ['name', 'eng', 'mat']])

# 다른 개체로 복사
df2 = df.loc[0:4, ['name', 'mat', 'eng']]
print(df2)

print("-------------------------------------------------------")
# 데이터 추가 : dict타입으로 추가
# list타입은 추가를 하면 자기가 바뀜
# dataframe은 새로운 항목을 추가한 객체를 반환하는 구조
# 반환값을 받아야 추가가 됨
# 데이터가 추가되면 인덱스를 새로 부여해야하는데
# 기존 인덱스를 무시할까요? 라는 의미 
# ignore_index=True 반드시 기재해야 함
df = df.append({"name":"김동현", "kor":99, "eng":90, "mat":100}, ignore_index=True)
print(df)

df.append({"name":"이서연", "kor":99, "eng":90, "mat":100}, ignore_index=True)
print(df)

# 컬럼명 확인하기
print(df.columns)

# 새로운 컬럼명 부여하기
df.columns = ["이름", "국어", "영어", "수학"]
print(df)

# 새로운 컬럼 추가
df["합계"] = df["국어"] + df["영어"] + df["수학"]
df["평균"] = round(df["합계"]/3, 1)
print(df)

 