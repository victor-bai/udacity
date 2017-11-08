from math import sqrt,acos,pi
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    CANNOT_NORMALIZED_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG = 'Only defined in two and three dimision'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __getitem__(self, item):
        if item >= len(self.coordinates):
            raise IndexError("out of index")
        value = self.coordinates[item]
        return value

    def plus(self, v):# Vector addition
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):# Vector substration
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):# A vector multiple a number
        new_coordinates = [Decimal(c)*x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):  # The vector's length
        coordinates_squared = [x**2 for x in self.coordinates]
        sqrt(4)
        return sum(coordinates_squared).sqrt()

    def normalized(self):  # Vector normalization
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal('1.0')/ magnitude)

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dot(self, v):  # A vector multiple a vector
        coordinates_multiple = [x*y for x,y in zip(self.coordinates, v.coordinates)]
        return sum(coordinates_multiple)

    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_radians = acos(u1.dot(u2))

            if in_degrees:
                degrees_per_radian = 180. / pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZED_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self,v):
        return (self.is_zero() or
                v.is_zero() or
                self.angle_with(v) == 0 or
                self.angle_with(v) == pi )

    def is_zero(self, tolerance = 1e-10):
        return self.magnitude() < tolerance

    def component_parallel_to(self, basis):
        try:
            u = basis.normalized()
            weight = self.dot(u)
            return u.times_scalar(weight)

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZED_ZERO_VECTOR_MSG:
                raise Exception(self.CANNOT_NORMALIZED_ZERO_VECTOR_MSG)
            else:
                raise e

    def component_orthognal_to(self, basis):
        try:
            projection = self.component_parallel_to(basis)
            return self.minus(projection)

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZED_ZERO_VECTOR_MSG:
                raise Exception(self.CANNOT_NORMALIZED_ZERO_VECTOR_MSG)
            else:
                raise e

    def cross(self, v):
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates
            new_coordinates = [ y_1*z_2 - y_2*z_1,
                               -(x_1*z_2 - x_2*z_1),
                               x_1*y_2 - x_2*y_1  ]
            return Vector(new_coordinates)

        except ValueError as e:
            msg = str(e)
            if msg == 'need more than 2 values to unpack':
                self_embedded_in_R3 = Vector(self.coordinates + ('0',))
                v_embedded_in_R3 = Vector(v.coordinates + ('0',))
                return self_embedded_in_R3.cross(v_embedded_in_R3)
            elif (msg == 'too many values to unpack' or
                   msg == 'need more than 1 value to unpack'):
                raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
            else:
                raise e

    def area_of_triangle_with(self, v):
        return self.area_of_parallelogram_with(v) / Decimal('2.0')

    def area_of_parallelogram_with(self, v):
        cross_product = self.cross(v)
        return cross_product.magnitude()

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def __getitem__(self, item):
        return self.coordinates[item]