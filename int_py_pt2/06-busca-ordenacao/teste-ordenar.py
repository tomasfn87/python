import pytest
import ordenar

class TesteOrdenar:

    @pytest.fixture
    def ord(self):
        return ordenar.Ordenar()

    @pytest.mark.parametrize("lista_a_ordenar, resultado", [
        ([1,2,3,5,4], [1,2,3,4,5]),
        ([0,-1,2,-3,4], [-3,-1,0,2,4]),
        ([10,20,11,5], [5,10,11,20]),
        ([2,3,1,0,-4], [-4,0,1,2,3]),
        ([0,-10,100,-100,4,8], [-100,-10,0,4,8,100]),
        ([1,1,1,1,1,1,0,1,1,1,1,-1], [-1,0,1,1,1,1,1,1,1,1,1,1]),
        ([2,0,1,0,9,8], [0,0,1,2,8,9]),
        ([2,3,6,7,3,1,6], [1,2,3,3,6,6,7]),
        (["sapo", "pato", "rato"], ["pato", "rato", "sapo"]),
        (["Z", "f", "z", "A", "F", "a"], ["A", "F", "Z", "a", "f","z"]),
    ])

    def teste_ordenar(self, lista_a_ordenar, resultado, ord):
        assert ord.selecao_direta(lista_a_ordenar) == resultado
        assert ord.bolha_curta(lista_a_ordenar)    == resultado
        assert ord.bolha(lista_a_ordenar)          == resultado
        assert ord.insertion(lista_a_ordenar)      == resultado
