# 행렬클래스
class Matrix:
    def __init__(self, mat1=None):
        if mat1 == None:
            self.mat1 = [ [1,2,3], [4,5,6], [7,8,9] ]
        else:
            self.mat1 = mat1
    
    def output(self):
        for i in range(0, len(self.mat1)):
            for j in range(0, len(self.mat1[i])):
                print("{0}  ".format(self.mat1[i][j]), end="")
            print()

    # m3 = m1 + m2 -> __add__ 호출
    def __add__(self, other):
        temp = list(list())     # 2차원 형태
        for i in range(0, len(self.mat1)):
            item = list()
            for j in range(0, len(self.mat1[i])):
                item.append(self.mat1[i][j] + other.mat1[i][j])
            temp.append(item)
        return Matrix(temp)     # 객체 만들어서 반환
                
m1 = Matrix()
m2 = Matrix( [[1,2,3], [4,5,6], [7,8,9]] )
m1.output()
m2.output()
print()
# m3 = m1.add(m2)     # m3 = m1 + m2
m3 = m1 + m2
m3.output()