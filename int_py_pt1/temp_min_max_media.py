# 1 - Quebrar o problema em problemas menores:
# Temp mínima e temp máxima:
# 2 - Testes automatizados
# 3 - Refatoração
# 4 - Eliminar código duplicado

def temperatura_min_max(temperaturas):
    print('A menor temperatura do mês foi', minima(temperaturas), 'ºC.')
    print('A maior temperatura do mês foi', maxima(temperaturas), 'ºC.')

def minima(temperaturas):
    min = temperaturas[0]
    # Defini um valor absurdamente alto para não ter problemas com
    # valores negativos.
    c1 = 0
    # Contador 1 - percorre os elementos da lista temperaturas
    while c1 < len(temperaturas):
        if temperaturas[c1] < min:
            min = temperaturas[c1]
        c1 += 1
    return min

def maxima(temperaturas):
    max = temperaturas[0]
    # Defini um valor absurdamente baixo para não ter problemas com
    # valores positivos.
    c2 = 0
    # Contador 2 - percorre os elementos da lista temperaturas
    while c2 < len(temperaturas):
        if temperaturas[c2] > max:
            max = temperaturas[c2]
        c2 += 1
    return max

# testa se minima(temperaturas) retorna o valor mínimo correto
def min_unit(temperaturas, valor_correto):
    assert minima(temperaturas) == valor_correto

# testa se maxima(temperaturas) retorna o valor máximo correto
def max_unit(temperaturas, valor_correto):
    assert maxima(temperaturas) == valor_correto

# Testes do py.test: -{
def test_minima_01():
    min_unit([10, 11, 12], 10)

def test_minima_02():
    min_unit([-5, 0, 5], -5)

def test_minima_03():
    min_unit([10, 100, 1000], 10)

def test_minima_04():
    min_unit([0, 0, 0], 0)

def test_maxima_01():
    max_unit([10, 11, 12], 12)

def test_maxima_02():
    max_unit([-5, 0, 5], 5)

def test_maxima_03():
    max_unit([10, 100, 1000], 1000)

def test_maxima_04():
    max_unit([0, 0, 0], 0)
# }-

# Digitar py.test nome_do_arquivo.py no terminal para rodar o py.test
# para esse um arquivo. O py.test procura as funções  iniciadas por
# 'test'. O py.test deve estar instalado.