import pytest

def merge_sort(lista):
        if len(lista) <= 1:        # base da recursão
            return lista
        
        meio = len(lista) // 2

        lado_esquerdo = merge_sort(lista[:meio])
        lado_direito = merge_sort(lista[meio:])

        return merge(lado_esquerdo, lado_direito)

def merge(lado_esquerdo, lado_direito):
    if not lado_esquerdo:
        return lado_direito
    
    if not lado_direito:
        return lado_esquerdo
    
    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)
    
    return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])

@pytest.mark.parametrize("input_ul, output_ol", [
    ([3, 1, 2, 5, 6, 4, 9, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([9, 1, 6, 3, 5, 4, 8, 2, 7], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([3, 1, 2, 5, 4, 7, 8, 9, 6], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1, 5, 2, 7, 6, 8, 4, 3, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([2, 6, 5, 3, 1, 9, 8, 7, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([100, 50, 200, 150, 300, -50, 0], [-50, 0, 50, 100, 150, 200, 300]),
    ([0, 100, 50, 150, 300, -50, 200], [-50, 0, 50, 100, 150, 200, 300])
])
def test_merge_sort(input_ul, output_ol):
    assert merge_sort(input_ul) == output_ol