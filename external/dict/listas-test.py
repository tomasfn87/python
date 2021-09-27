import pytest
import listas

class TesteListas:
    @pytest.fixture
    def L(self):
        return listas.Listas

    @pytest.mark.parametrize("lista, resultado", [
        (["product", "value"], {"product": "", "value": ""}),
        (["firstname", "lastname"], {"firstname": "", "lastname": ""}),
        (["height", "width"], {"height": "", "width": ""})
    ])
    def test_criar_chaves(self, lista, resultado, L):
        assert L.criar_chaves(lista) == resultado

    @pytest.mark.parametrize("dicionario, lista, resultado", [
        ({"product": "", "value": ""}, ["beer", "$2.25"], {"product": "beer", "value": "$2.25"}),
        ({"firstname": "", "lastname": ""}, ["Ivan", ", the terrible"], {"firstname": "Ivan", "lastname": ", the terrible"}),
        ({"height": "", "width": ""}, ["160px", "220px"], {"height": "160px", "width": "220px"})
    ])
    def test_atribuir_valores_simples(self, dicionario, lista, resultado, L):
        assert L.atribuir_valores(dicionario, lista) == resultado

    @pytest.mark.parametrize("dicionario, lista, novo, resultado, dicionario_original", [
        ({"product": "", "value": ""}, ["beer", "$2.25"], True, {"product": "beer", "value": "$2.25"}, {"product": "", "value": ""}),
        ({"firstname": "", "lastname": ""}, ["Ivan", ", the terrible"], True, {"firstname": "Ivan", "lastname": ", the terrible"}, {"firstname": "", "lastname": ""}),
        ({"height": "", "width": ""}, ["160px", "220px"], True, {"height": "160px", "width": "220px"}, {"height": "", "width": ""}),
        ({"product": "", "value": ""}, ["beer", "$2.25"], False, {"product": "beer", "value": "$2.25"}, {"product": "beer", "value": "$2.25"}),
        ({"firstname": "", "lastname": ""}, ["Ivan", ", the terrible"], False, {"firstname": "Ivan", "lastname": ", the terrible"}, {"firstname": "Ivan", "lastname": ", the terrible"}),
        ({"height": "", "width": ""}, ["160px", "220px"], False, {"height": "160px", "width": "220px"}, {"height": "160px", "width": "220px"})
    ])
    def test_atribuir_valores_completo(self, dicionario, lista, novo, resultado, dicionario_original, L):
        assert L.atribuir_valores(dicionario, lista, novo) == resultado \
            and dicionario == dicionario_original

    @pytest.mark.parametrize("lista_chaves, lista_valores, resultado", [
        (["product", "value"], ["beer", "$2.25"], {"product": "beer", "value": "$2.25"}),
        (["firstname", "lastname"], ["Ivan", ", the terrible"], {"firstname": "Ivan", "lastname": ", the terrible"}),
        (["height", "width"], ["160px", "220px"], {"height": "160px", "width": "220px"}),
    ])
    def test_criar_dicionario(self, lista_chaves, lista_valores, resultado, L):
        assert L.criar_dicionario(lista_chaves, lista_valores) == resultado

    @pytest.mark.parametrize("dicionario, resultado", [
        ({"product": "beer", "value": "$2.25"}, ["product", "value"]),
        ({"firstname": "Ivan", "lastname": ", the terrible"}, ["firstname", "lastname"]),
        ({"height": "160px", "width": "220px"}, ["height", "width"]),
    ])
    def test_obter_chaves(self, dicionario, resultado, L):
        assert L.obter_chaves(dicionario) == resultado

    @pytest.mark.parametrize("dicionario, resultado", [
        ({"product": "beer", "value": "$2.25"}, ["beer", "$2.25"]),
        ({"firstname": "Ivan", "lastname": ", the terrible"}, ["Ivan", ", the terrible"]),
        ({"height": "160px", "width": "220px"}, ["160px", "220px"])
    ])
    def test_obter_valores(self, dicionario, resultado, L):
        assert L.obter_valores(dicionario) == resultado