class Parametrization(object):
    BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM_MSG = ('The basepoint and direction vectors should all live in the same dimension')

    def __init__(self, basepoint, direction_vectors):
        self.basepoint = basepoint
        self.direction_vectors = direction_vectors
        self.dimension = self.basepoint.dimension

        try:
            for v in direction_vectors:
                assert v.dimension == self.dimension
        except AssertionError:
            raise Exception(self.BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM_MSG)

    def __str__(self):
        ret = ''
        temp = ['x_{}={}'.format(i+1,round(p,3)) for i,p in enumerate(self.basepoint)]
        temp2 = [ '{} * x_{}'.format(c,v) for c,v in enumerate(self.direction_vectors)]
        ret += '\n'.join(temp2)
        return ret