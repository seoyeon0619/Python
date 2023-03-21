import pandas as pd
import numpy as np
# df = pd.read_csv("./data/서울특별시 성북구_노점상(거리가게) 허가 현황 및 정보_20220211.csv", encoding="cp949")
# print(df.head())

s = pd.Series([1, 2, 3, np.nan, 5, 6, np.nan])
print(s)

# 각 요소가 Nan이면 True, Nan이 아니면 False를 반환
print(s.isnull())

# 결과가 True인 것의 개수 
print(s.isnull().sum())

# 데이터프레임
# 하나의 필드라도 null이 있으면 그 행을 삭제하는 방법
# 그 비율이 너무 높은 경우 삭제 불가
# 평균값(비범주형) 또는 중간값(비범주형), 최빈값(범주형)으로 대체하는 방법
data = pd.read_csv("./data/data.csv")
print(data.head())

# 데이터 누락치 확인 가능
print(data.info())

# 필드에 Nan값 확인방법
# dropna = False : Nan값도 카운트 해줌 (카테고리 타입에 적합)
print(data["height"].value_counts(dropna=False))
# dropna = True : Nan값은 카운트 안함
print(data["height"].value_counts(dropna=True))
# Nan일때 True
print(data["height"].isnull())
# Nan일때 True
print(data["weight"].notnull())

# Nan값 카운트
print(data["height"].isnull().sum())
print(data["weight"].isnull().sum())
print(data.isnull().sum())

# 처리방법1 : 삭제
# axis=1 : 열
# Nan값을 포함한 열이 있으면 삭제
# thresh : 삭제 배제 조건 (Nan이 아닌 데이터가 최소 28건 이상이어야 함)
data2 = data.dropna(axis=1, thresh=28)       
print(data2)

# axis=0 : 행
data3 = data.dropna(axis=0)
print(data3.shape)
print(data3["weight"].isnull().sum())

data3 = data.dropna(axis=0, thresh=2)
print(data3.shape)
print(data3["weight"].isnull().sum())

data2 = data.dropna(subset=["height"], how='any', axis=0)
print(data2.shape)

data2 = data.dropna(subset=["height", 'weight'], how='any', axis=0)
print(data2.shape)


