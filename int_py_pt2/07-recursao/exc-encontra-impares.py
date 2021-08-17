import pytest

def encontra_impares(lista, apenas_impares=False):
    if apenas_impares == True:
        return lista[:]
    else:
        impares = []
        for i in lista[:]:
            if i % 2 != 0:
                impares.append(i)
        return encontra_impares(impares, True)


@pytest.mark.parametrize("lista, impares",[
    ([1, 2, 3, 4, 5, 6, 7], [1, 3, 5, 7]),
    ([1, 3, 5, 7], [1, 3, 5, 7]),
    ([3, 2, 21, 44, 47, 89, 91, 8, 100], [3, 21, 47, 89, 91]),
    ([21, 22, 23, 25, 28, 28, 29, 30], [21, 23, 25, 29])
])
def test_encontra_impares(lista, impares):
    assert encontra_impares(lista) == impares