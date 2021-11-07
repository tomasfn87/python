import pytest
import listas

class TesteListas:
    @pytest.fixture
    def L(self):
        return listas.Listas

    @pytest.mark.parametrize("lista, resultado", [
        (["firstname", "lastname"], {"firstname": "", "lastname": ""}),
        (["product", "value"], {"product": "", "value": ""}),
        (["height", "width"], {"height": "", "width": ""})
    ])
    def test_criar_chaves(self, lista, resultado, L):
        assert L.criar_chaves(lista) == resultado

    @pytest.mark.parametrize("dicionario, lista, resultado", [
        ({"firstname": "", "lastname": ""}, ["Ivan", ", the terrible"], {"firstname": "Ivan", "lastname": ", the terrible"}),
        ({"product": "", "value": ""}, ["beer", "$2.25"], {"product": "beer", "value": "$2.25"}),
        ({"height": "", "width": ""}, ["160px", "220px"], {"height": "160px", "width": "220px"})
    ])
    def test_atribuir_valores_simples(self, dicionario, lista, resultado, L):
        assert L.atribuir_valores(dicionario, lista) == resultado

    @pytest.mark.parametrize("dicionario, lista, novo, resultado, dicionario_original", [
        ({"firstname": "", "lastname": ""}, ["Ivan", ", the terrible"], True, {"firstname": "Ivan", "lastname": ", the terrible"}, {"firstname": "", "lastname": ""}),
        ({"product": "", "value": ""}, ["beer", "$2.25"], True, {"product": "beer", "value": "$2.25"}, {"product": "", "value": ""}),
        ({"height": "", "width": ""}, ["160px", "220px"], True, {"height": "160px", "width": "220px"}, {"height": "", "width": ""}),
        ({"firstname": "", "lastname": ""}, ["Ivan", ", the terrible"], False, {"firstname": "Ivan", "lastname": ", the terrible"}, {"firstname": "Ivan", "lastname": ", the terrible"}),
        ({"product": "", "value": ""}, ["beer", "$2.25"], False, {"product": "beer", "value": "$2.25"}, {"product": "beer", "value": "$2.25"}),
        ({"height": "", "width": ""}, ["160px", "220px"], False, {"height": "160px", "width": "220px"}, {"height": "160px", "width": "220px"})
    ])
    def test_atribuir_valores_completo(self, dicionario, lista, novo, resultado, dicionario_original, L):
        assert L.atribuir_valores(dicionario, lista, novo) == resultado \
            and dicionario == dicionario_original

    @pytest.mark.parametrize("lista_chaves, lista_valores, resultado", [
        (["firstname", "lastname"], ["Ivan", ", the terrible"], {"firstname": "Ivan", "lastname": ", the terrible"}),
        (["product", "value"], ["beer", "$2.25"], {"product": "beer", "value": "$2.25"}),
        (["height", "width"], ["160px", "220px"], {"height": "160px", "width": "220px"}),
    ])
    def test_criar_dicionario(self, lista_chaves, lista_valores, resultado, L):
        assert L.criar_dicionario(lista_chaves, lista_valores) == resultado

    @pytest.mark.parametrize("dicionario, resultado", [
        ({"firstname": "Ivan", "lastname": ", the terrible"}, ["firstname", "lastname"]),
        ({"product": "beer", "value": "$2.25"}, ["product", "value"]),
        ({"height": "160px", "width": "220px"}, ["height", "width"]),
    ])
    def test_obter_chaves(self, dicionario, resultado, L):
        assert L.obter_chaves(dicionario) == resultado

    @pytest.mark.parametrize("dicionario, resultado", [
        ({"firstname": "Ivan", "lastname": ", the terrible"}, ["Ivan", ", the terrible"]),
        ({"product": "beer", "value": "$2.25"}, ["beer", "$2.25"]),
        ({"height": "160px", "width": "220px"}, ["160px", "220px"])
    ])
    def test_obter_valores(self, dicionario, resultado, L):
        assert L.obter_valores(dicionario) == resultado
    
    @pytest.mark.parametrize("dictArr, key, resultado", [
        ([{'chave1': 'Ac'}, {'chave1': 'Aa'}, {'chave1': 'Ab'}], "chave1", [{'chave1': 'Aa'}, {'chave1': 'Ab'}, {'chave1': 'Ac'}]),
        ([{'chave1': 'Ba'}, {'chave1': 'Bb'}, {'chave1': 'Bc'}, {'chave1': 'Aa'}, {'chave1': 'Ab'}, {'chave1': 'Ac'}], "chave1", [{'chave1': 'Aa'}, {'chave1': 'Ab'}, {'chave1': 'Ac'}, {'chave1': 'Ba'}, {'chave1': 'Bb'}, {'chave1': 'Bc'}])
    ])
    def test_sortDictsByKey(self, dictArr, key, resultado, L):
        assert L.sortDictsByKey(dictArr, key) == resultado
    
    @pytest.mark.parametrize("dictArr, key, resultado", [
        ([{'chave1': 'Ac'}, {'chave1': 'Aa'}, {'chave1': 'Ab'}], "chave1", True),
        ([{'chave1': 'Ba'}, {'chave1': 'Bb'}, {'chave1': 'Bc'}, {'chave1': 'Aa'}, {'chave1': 'Ab'}, {'chave1': 'Ac'}], "chave1", True),
        ([{'chave2': 'Ac'}, {'chave1': 'Aa'}, {'chave1': 'Ab'}], "chave1", False),
        ([{'chave2': 'Ba'}, {'chave1': 'Bb'}, {'chave1': 'Bc'}, {'chave1': 'Aa'}, {'chave1': 'Ab'}, {'chave1': 'Ac'}], "chave1", False),
        ([{'chave1': 'Ac'}, {'chave1': 'Aa'}, {'chave1': 'Ab'}], "chave2", False),
        ([{'chave1': 'Ba'}, {'chave1': 'Bb'}, {'chave1': 'Bc'}, {'chave1': 'Aa'}, {'chave1': 'Ab'}, {'chave1': 'Ac'}], "chave2", False)
    ])
    def test_dictsHaveKey(self, dictArr, key, resultado, L):
        assert L.dictsHaveKey(dictArr, key) == resultado
    
    @pytest.mark.parametrize("lista, resultado", [
        ([{"nome": "Fernanda", "cabelo": "castanho"},{"nome": "Alice", "cabelo": "loiro"},{"nome": "Ana", "cabelo": "preto"}], 16)
    ])
    def test_analisarListaDict_simples(self, lista, resultado, L):
        assert L.analisarListaDict(lista) == resultado
    
    @pytest.mark.parametrize("lista, chaves, resultado", [
        ([{"nome": "Fernanda", "cabelo": "castanho"},{"nome": "Alice", "cabelo": "loiro"},{"nome": "Ana", "cabelo": "preto"}], ["nome", "cabelo"], 16),
        ([{"nome": "Fernanda", "cabelo": "castanho"},{"nome": "Alice", "cabelo": "loiro"},{"nome": "Ana", "cabelo": "preto"}], ["nome"], 8)
    ])
    def test_analisarListaDict_completo(self, lista, chaves, resultado, L):
        assert L.analisarListaDict(lista, chaves) == resultado