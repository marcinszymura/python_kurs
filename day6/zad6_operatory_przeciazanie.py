class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise NotImplementedError()


class TestVector:
    def test_init(self):
        vector = Vector(1, 2)
        assert vector.x == 1
        assert vector.y == 2

    def test_add_two_vectors(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        v3 = v1 + v2
        assert v3.x == 4
        assert v3.y == 6

    def test_sub_two_vectors(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        v3 = v1 - v2
        assert v3.x == -2
        assert v3.y == -2