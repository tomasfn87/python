import Bhaskara
import pytest

class TestBhaskara:

    @pytest.fixture
    def b(self):
        return Bhaskara.Bhaskara
    
    def test_Bhaskara_01(self):
        assert b.calcular_raizes(4, 4, 4) == 0

    def test_Bhaskara_02(self, b):
        assert b.calcular_raizes(1, 0, 0) == (1, 0)

    def test_Bhaskara_03(self, b):
        assert b.calcular_raizes(4, 12, 9) == (1, -1.5)

    def test_Bhaskara_04(self, b):
        assert b.calcular_raizes(4, 2, -6) == (2, 1.0, -1.5)

'''
print(Bhaskara.Bhaskara.calcular_raizes(4, 4, 4))
print(Bhaskara.Bhaskara.calcular_raizes(4, 2, -6))
print(Bhaskara.Bhaskara.calcular_raizes(4, 12, 9))
'''