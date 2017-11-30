import unittest
import numpy as np

class Bai:
    def __init__(self):
        pass

    def swapRows(self, M, r1, r2):
        M[r1], M[r2] = M[r2], M[r1]

a = [[1,2,3],
     [2,2,2]]
bai = Bai()
print 0 <1.0e-16