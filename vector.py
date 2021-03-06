import math


class Vector:

    def __init__(self, *coordinate):
        if len(coordinate) != 0:
            for number in coordinate:
                if type(number) not in (int, float):
                    raise ValueError
            self.vector = tuple(coordinate)
        else:
            raise ValueError

    def __str__(self):
        return str(self.vector)

    def __add__(self, other):
        if type(other) == Vector and len(self.vector) == len(other.vector):
            result = []
            for i in range(len(self.vector)):
                result.append(self.vector[i]+other.vector[i])
            vec = Vector(0)
            vec.vector = tuple(result)
            return vec

        else:
            raise ValueError

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __sub__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other.__mul__(-1))

    def __rsub__(self, other):
        return other.__sub__(self)

    def __mul__(self, other):
        if type(other) == float or type(other) == int:
            result = []
            for i in range(len(self.vector)):
                result.append(self.vector[i]*other)
            vec = Vector(0)
            vec.vector = tuple(result)
            return vec
        else:
            raise ValueError

    def __rmul__(self, other):
        return self.__mul__(other)

    def __mod__(self, other):
        if type(other) == float or type(other) == int:
            result = []
            for i in range(len(self.vector)):
                result.append(self.vector[i] % other)
            vec = Vector(0)
            vec.vector = tuple(result)
            return vec
        else:
            raise ValueError

    def dist(self, other):
        if len(self.vector) == len(other.vector):
            total = 0
            for i in range(len(self.vector)):
                total += (self.vector[i]-other.vector[i])**2
            return math.sqrt(total)
        else:
            raise ValueError

    def norm(self):
        total = 0
        for i in range(len(self.vector)):
            total += (self.vector[i]) ** 2
        return math.sqrt(total)

    def renorm(self, new_norm):
        if self.norm() == 0: return self
        else:
            return self*(1/self.norm())*new_norm


if __name__ == "__main__":
    vec1 = Vector(1, 1, 1)
    vec2 = Vector(2, 2, 2)
    vec2 += Vector(1, 2, 3)
    scal = 2.5
    print(vec2.dist(vec1))
