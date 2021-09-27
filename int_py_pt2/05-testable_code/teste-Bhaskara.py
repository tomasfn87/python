import Bhaskara
import pytest

class TestBhaskara:

    @pytest.fixture
    def bha(self):
        return Bhaskara.Bhaskara

    @pytest.mark.parametrize("a, b, c, result", [
        (4, 4, 4, 0),
        (10, 10, 10, 0),
        (1, 0, 0, (1, 0)),
        (4, 12, 9, (1, -1.5)),
        (4, 2, -6, (2, 1.0, -1.5)),
        (8, 4, -4, (2, 0.5, -1.0)),
        (4, 2, -2, (2, 0.5, -1.0)),
        (1, 36, 324, (1, -18)),
        (3, 36, 108, (1, -6)),
        (1, 28, 196, (1, -14)),
        (4, 28, 49, (1, -3.5)),
        (49, 28, 4, (1, -0.2857142857142857))
    ])

    def test_Bhaskara(self, a, b, c, result, bha):
        assert bha.calcular_raizes(a, b, c) == result

    '''
    def test_Bhaskara_01(self, bha):
        assert bha.calcular_raizes(4, 4, 4) == 0

    def test_Bhaskara_02(self, bha):
        assert bha.calcular_raizes(1, 0, 0) == (1, 0)

    def test_Bhaskara_03(self, bha):
        assert bha.calcular_raizes(4, 12, 9) == (1, -1.5)

    def test_Bhaskara_04(self, bha):
        assert bha.calcular_raizes(4, 2, -6) == (2, 1.0, -1.5)
    '''