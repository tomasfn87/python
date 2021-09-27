import pytest
import listas

@pytest.fixture
def criar_chaves():
    return listas.criar_chaves
@pytest.fixture
def atribuir_valores():
    return listas.atribuir_valores
@pytest.fixture
def criar_dicionario():
    return listas.criar_dicionario
@pytest.fixture
def obter_chaves():
    return listas.obter_chaves
@pytest.fixture
def obter_valores():
    return listas.obter_valores

@pytest.mark.parametrize("lista, resultado", [
    (["product", "value"], {"product": "", "value": ""}),
    (["firstname", "lastname"], {"firstname": "", "lastname": ""}),
    (["height", "width"], {"height": "", "width": ""})
])
def test_criar_chaves(lista, resultado, criar_chaves):
    assert criar_chaves(lista) == resultado

@pytest.mark.parametrize("dicionario, lista, resultado", [
    ({"product": "", "value": ""}, ["beer", "$2.25"], {"product": "beer", "value": "$2.25"}),
    ({"firstname": "", "lastname": ""}, ["Ivan", ", the terrible"], {"firstname": "Ivan", "lastname": ", the terrible"}),
    ({"height": "", "width": ""}, ["160px", "220px"], {"height": "160px", "width": "220px"})
])
def test_atribuir_valores_simples(dicionario, lista, resultado, atribuir_valores):
    assert atribuir_valores(dicionario, lista) == resultado

@pytest.mark.parametrize("dicionario, lista, novo, resultado, dicionario_original", [
    ({"product": "", "value": ""}, ["beer", "$2.25"], True, {"product": "beer", "value": "$2.25"}, {"product": "", "value": ""}),
    ({"firstname": "", "lastname": ""}, ["Ivan", ", the terrible"], True, {"firstname": "Ivan", "lastname": ", the terrible"}, {"firstname": "", "lastname": ""}),
    ({"height": "", "width": ""}, ["160px", "220px"], True, {"height": "160px", "width": "220px"}, {"height": "", "width": ""}),
    ({"product": "", "value": ""}, ["beer", "$2.25"], False, {"product": "beer", "value": "$2.25"}, {"product": "beer", "value": "$2.25"}),
    ({"firstname": "", "lastname": ""}, ["Ivan", ", the terrible"], False, {"firstname": "Ivan", "lastname": ", the terrible"}, {"firstname": "Ivan", "lastname": ", the terrible"}),
    ({"height": "", "width": ""}, ["160px", "220px"], False, {"height": "160px", "width": "220px"}, {"height": "160px", "width": "220px"})
])
def test_atribuir_valores_completo(dicionario, lista, novo, resultado, dicionario_original, atribuir_valores):
    assert atribuir_valores(dicionario, lista, novo) == resultado \
    and dicionario == dicionario_original

@pytest.mark.parametrize("lista_chaves, lista_valores, resultado", [
    (["product", "value"], ["beer", "$2.25"], {"product": "beer", "value": "$2.25"}),
    (["firstname", "lastname"], ["Ivan", ", the terrible"], {"firstname": "Ivan", "lastname": ", the terrible"}),
    (["height", "width"], ["160px", "220px"], {"height": "160px", "width": "220px"}),
])
def test_criar_dicionario(lista_chaves, lista_valores, resultado, criar_dicionario):
    assert criar_dicionario(lista_chaves, lista_valores) == resultado

@pytest.mark.parametrize("dicionario, resultado", [
    ({"product": "beer", "value": "$2.25"}, ["product", "value"]),
    ({"firstname": "Ivan", "lastname": ", the terrible"}, ["firstname", "lastname"]),
    ({"height": "160px", "width": "220px"}, ["height", "width"]),
])
def test_obter_chaves(dicionario, resultado, obter_chaves):
    assert obter_chaves(dicionario) == resultado

@pytest.mark.parametrize("dicionario, resultado", [
    ({"product": "beer", "value": "$2.25"}, ["beer", "$2.25"]),
    ({"firstname": "Ivan", "lastname": ", the terrible"}, ["Ivan", ", the terrible"]),
    ({"height": "160px", "width": "220px"}, ["160px", "220px"])
])
def test_obter_valores(dicionario, resultado, obter_valores):
    assert obter_valores(dicionario) == resultado