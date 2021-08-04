import triangulo
import pytest

class TesteTriangulo:

    @pytest.fixture
    def tri(self):
        return triangulo.Triangulo

    @pytest.mark.parametrize("a, b, c, res_perim, res_tipo, res_retan", [
        (1.2, 1.2, 1.2, 3*1.2, "equilátero", False),
        (1.5, 1.5, 3, 6, "isósceles", False),
        (2, 2, 2, 6, "equilátero", False),
        (2, 2, 4, 8, "isósceles", False),
        (2.5, 2.5, 2.5, 7.5, "equilátero", False),
        (3, 4, 5, 12, "escaleno", True),
        (5, 5, 5, 15, "equilátero", False),
        (5, 5, 9, 19, "isósceles", False),
        (5, 6, 7, 18, "escaleno", False),
        (5, 5.5, 7.5, 18, "escaleno", False),
        (6, 8, 10, 24, "escaleno", True),
        (10.5, 10.5, 10.5, 31.5, "equilátero", False),
        (11, 11, 11, 33, "equilátero", False),
        (11, 11, 18, 40, "isósceles", False),
        (12, 15, 18, 45, "escaleno", False),
        (15, 20, 25, 60, "escaleno", True),
        (100, 100, 100, 300, "equilátero", False),
        (115, 115, 70, 300, "isósceles", False),
        (130, 100, 70, 300, "escaleno", False),
        (150, 200, 250, 600, "escaleno", True),
        (200, 150, 250, 600, "escaleno", True)
    ])
    def test_Triangulo(self, a, b, c, res_perim, res_tipo, res_retan, tri):
        assert tri(a, b, c).perimetro() == res_perim \
           and tri(a, b, c).tipo_lado() == res_tipo \
           and tri(a, b, c).retangulo() == res_retan
    
    @pytest.mark.parametrize("a, d, b, e, c, f, res_semel", [
        (2, 20, 4, 8, 5, 16, True),
        (2, 4, 3, 6, 5, 10, True),
        (2, 5, 3, 6, 5, 10, False),
        (5, 7.5, 7, 10.5, 11, 16.5, True),
        (5, 11, 8, 17, 12, 25, False),
        (10, 50, 20, 100, 30, 150, True),
        (10, 40, 20, 80, 30, 130, False),
        (7, 30, 15, 14, 10, 20, True),
        (21, 15, 45, 7, 30, 10, True)
    ])
    def test_semelhantes(self, a, b, c, d, e, f, res_semel, tri):
        t1, t2 = tri(a, b, c), tri(d, e, f)
        assert t1.semelhantes(t2) == res_semel