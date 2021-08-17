import pytest

def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        if len(lista) < 1:
            return False
        else:
            soma = lista[:]
            soma[0] += soma[-1]
            del soma[-1]
            return soma_lista(soma)

@pytest.mark.parametrize("lista, soma_elementos_lista", [
    ([1, 2, 3, 4], 10),
    ([2, 2, 2, 4], 10),
    ([3, 3, 2, 2], 10),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10),
    ([0, 10], 10),
    ([3, 3, 3], 9),
    ([1, 1, 7], 9),
    ([2, 2, 5], 9),
    ([10, 20, -21], 9),
    ([25, 25, 25, 25], 100),
    ([25, 50, 10, 15], 100),
    ([10, 10, 10, 70], 100),
    ([20, 20, 30, 30], 100)
])
def test_soma_lista(lista, soma_elementos_lista):
    assert soma_lista(lista) == soma_elementos_lista
