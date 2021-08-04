class Triangulo:
    def __init__(self, a, b, c):
        assert type(a) == int or type(a) == float
        self.a = a
        assert type(b) == int or type(b) == float
        self.b = b
        assert type(c) == int or type(c) == float
        self.c = c

    def a(self):
        return self.a

    def a(self):
        return self.b

    def a(self):
        return self.c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b == self.c:
            return "equilátero"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "isósceles"
        else:
            return "escaleno"