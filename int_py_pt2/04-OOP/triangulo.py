class Triangulo:
    def __init__(self, a, b, c):
        assert type(a) == int or type(a) == float and a > 0
        self.a = a
        assert type(b) == int or type(b) == float and b > 0
        self.b = b
        assert type(c) == int or type(c) == float and c > 0
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
        lados_self, lados_tri = [self.a, self.b, self.c], \
                                [triangulo.a, triangulo.b, triangulo.c]
        lados_self.sort()
        lados_tri.sort()
        if lados_self[0] / lados_tri[0] == \
           lados_self[1] / lados_tri[1] == \
           lados_self[2] / lados_tri[2]:
            return True
        else:
            return False