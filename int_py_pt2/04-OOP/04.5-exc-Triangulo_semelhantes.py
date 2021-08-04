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

    def tipo_lado(self):
        if self.a == self.b == self.c:
            return "equilátero"
        elif self.a == self.b \
          or self.a == self.c \
          or self.b == self.c:
            return "isósceles"
        else:
            return "escaleno"
    
    def retangulo(self):
        lados = [self.a, self.b, self.c]
        lados.sort()
        if lados[2] ** 2 == (lados[0] ** 2 + lados[1] ** 2):
            return True
        else:
            return False

    def semelhantes(self, triangulo):
        if   self.a / triangulo.a \
          == self.b / triangulo.b \
          == self.c / triangulo.c:
            return True
        else:
            return False