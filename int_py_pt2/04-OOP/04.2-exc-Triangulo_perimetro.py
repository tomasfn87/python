class Triangulo:
    def __init__(self, a, b, c):
        assert type(a) == int or type(a) == float
        self.a = a
        assert type(b) == int or type(b) == float
        self.b = b
        assert type(c) == int or type(c) == float
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c