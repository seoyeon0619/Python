import pandas as pd

df = pd.read_csv("./data/auto-mpg.csv")

# 앞 5행
print(df.head())

# 뒤 5행
print(df.tail())

# 각 필드들에 대한 간략한 설명
print(df.info())

# 기초 통계요약
print(df.describe())

print("---------------------------")

# 실린더 개수가 4인 데이터는 True 아니면 False 반환
print(df.cylinders == 4)

# 실린더 4개인 데이터 추출
print(df[df.cylinders == 4])

df2 = df[df.cylinders == 4]
print(df2.shape)
 
# 연비가 평균이 넘는 데이터만 추출
# 연비 평균 mpg 필드의 평균값 구하기
mpg_mean = df["mpg"].mean()
print("연비 평균", mpg_mean)

df3 = df[df.mpg >= mpg_mean]
print(df3.head())

# 연비와 마력이 평균이 넘는 것
import numpy as np

hp_mean = df["horsepower"].mean()
df3 = df[np.logical_and(df.mpg >= mpg_mean, df.horsepower >= hp_mean)] 
print(df3)

print("---------------------------")

irisData = pd.read_csv("./data/iris.csv")
print(irisData.info())
print(irisData.head(7))
print(irisData.describe())
print(irisData.shape)

temp = irisData[irisData["variety"] == "Setosa"]
print(temp)

temp = irisData[irisData["variety"] == "Setosa"]["sepal.length"]
print("Setosa평균 : ", temp.mean())
temp = irisData[irisData["variety"] == "Virginica"]["sepal.length"]
print("Virginica평균 : ", temp.mean())
temp = irisData[irisData["variety"] == "Versicolor"]["sepal.length"]
print("Versicolor평균 : ", temp.mean())

temp = irisData[irisData["variety"] == "Setosa"] and [irisData["sepal.length"] >= 5]
print("Stosa 5 이상 개수 : ", temp.count())

