# -- coding: utf-8 --
import numpy as np
from fractions import Fraction

class Bai:
    def __init__(self):
        pass

    def swapRows(self, M, r1, r2):
        M[r1], M[r2] = M[r2], M[r1]

    def matxRound(self, M, decPts=4):
        for i, row in enumerate(M):
            for j, col in enumerate(row):
                M[i][j] = round(col, decPts)

    def addScaledRow(self, M, r1, r2, scale):
        t = [M[r1][i] + M[r2][i] * scale for i in range(len(M[r1]))]
        M[r1] = t

    def scaleRow(self, M, r, scale):
        if scale == 0:
            raise ValueError
        M[r] = [x * scale for x in M[r]]

    def augmentMatrix(self, A, b):
        (r, c) = self.shape(A)
        augment = [[0 for i in range(c + 1)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                augment[i][j] = A[i][j]
            augment[i][c] = b[i][0]
        return augment

    def shape(self, M):
        row = 0
        col = 0
        for i in M:
            row += 1
        for j in M[0]:
            col += 1
        return row, col

    def transpose(self,M):
        (r, c) = self.shape(M)
        M_ = [[0 for i in range(r)] for i in range(c)]
        for i, row in enumerate(M_):
            for j, col in enumerate(row):
                M_[i][j] = M[j][i]
        return M_

    def matxMultiply(self, A, B):
        (ra, ca) = self.shape(A)
        (rb, cb) = self.shape(B)
        try:
            result = [[0 for i in range(cb)] for i in range(ra)]
            for i in range(ra):
                for c in range(cb):
                    temp = 0
                    for j in range(ca):
                        temp = temp + A[i][j] * B[j][c]
                    result[i][c] = temp
            return result
        except Exception as e:
            raise ValueError

    #对于Ab的每一列（最后一列除外）
    # 当前列为列c
    # 寻找列c中 对角线以及对角线以下所有元素（行 c~N）的绝对值的最大值
    # 如果绝对值最大值为0
    #     那么A为奇异矩阵，返回None (你可以在选做问题2.4中证明为什么这里A一定是奇异矩阵)
    # 否则
    #     使用第一个行变换，将绝对值最大值所在行交换到对角线元素所在行（行c）
    #     使用第二个行变换，将列c的对角线元素缩放为1
    #     多次使用第三个行变换，将列c的其他元素消为0
    def gj_Solve(self, A, b, decPts=4, epsilon=1.0e-16):
        if not len(A) == len(b):
            return None
        Ab = self.augmentMatrix(A, b)
        size = len(A[0])
        for col in range(size):
            max = 0
            maxIndex = 0
            for row in range(col,size):
                if abs(Ab[row][col]) > max:
                    max = abs(Ab[row][col])
                    maxIndex = row
            if max > epsilon:
                self.swapRows(Ab, col, maxIndex)
                self.scaleRow(Ab, col, Fraction(1,1)/Ab[col][col])
                for i in range(size):
                    if i == col:
                        continue
                    self.addScaledRow(Ab, i, col, -Ab[i][col])
            else:
                return None
            # print "第{}次：{}".format(col+1,np.asarray(Ab))
        res = [[0 for i in range(1)] for i in range(size)]
        for i in range(size):
            res[i][0] = Ab[i][size]
        return res

A = [[-8,2,-8,-1],
     [-2,4,3,5],
     [6,-4,-3,-2],
     [9,-2,-4,-1]]
B = [[-8,2,-8,-1],
     [-2,4,3,5],
     [6,-4,-3,-2],
     [9,-2,-4,-1]]
b = [[1],
     [1],
     [1],
     [1]]
bai = Bai()
x = bai.gj_Solve(A,b,epsilon=1.0e-8)
# print np.asarray(x)
# print np.dot(B,x)
a = [1,2,3]
b = [4,5,6]
c = (a,b)
b = [[1 for i in range(1)] for i in range(3)]
print x[0]