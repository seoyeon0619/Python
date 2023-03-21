import pickle

# 파일에 객체 저장하기
colors = {"red":"빨강", "green":"초록","blue":"파랑"}
file = open("test.bin", "wb")       # w-write, b-binary 파일을 이진으로 생성
pickle.dump(colors, file=file)
file.close()

# 파일에서 객체 읽기
colors = {}
file = open("test.bin", "rb")       # r-red, b-binary 파일을 이진으로 생성
colors = pickle.load(file=file)
file.close()