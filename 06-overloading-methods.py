class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Vector ({self.a},{self.b})'

    def __add__(self, other):
        return Vector(self.a + other.a, self.b+other.b)


v1 = Vector(3, 4)
v2 = Vector(4, -5)
v3 = Vector(4, 1)
print(v1+v2+v3)
