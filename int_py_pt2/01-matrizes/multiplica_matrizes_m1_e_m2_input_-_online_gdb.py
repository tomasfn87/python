def valores_matriz(num_linhas, num_colunas):
    ''' (int, int) Cria e retorna uma matriz com num_linhas linhas e 
    num_colunas colunas em que cada elemento é inserido pelo usuário.
    '''
    matriz  = []
    cont_linha = 1
    cont_coluna = 1
    for i in range(num_linhas):
        cont_coluna = 1
        linha = []
        for j in range(num_colunas):
            print(
                "Insira o valor do elemento "\
              + str(cont_coluna) + " da linha " + str(cont_linha) + ": "
            )
            linha.append(int(input()))
            cont_coluna += 1
        matriz.append(linha)
        cont_linha += 1
    return matriz

def cria_matriz():
    n_linhas = int(input('Insira o # de linhas: '))
    n_colunas = int(input('Insira o # de colunas: '))
    print()
    return valores_matriz(n_linhas, n_colunas)

def cria_matriz_a_multiplicar(m1):
    n_linhas = len(m1[0])
    n_colunas = int(input('Insira o # de colunas de m2: '))
    print()
    return valores_matriz(n_linhas, n_colunas)

def sao_multiplicaveis(m1, m2):
    if len(m1[0]) == len(m2):
       return True
    else:
        return False

def imprime_matriz(matriz):
    for linha in matriz:
        c = 0
        for elemento in linha:
            if c == len(matriz[0]) - 1:
                print(elemento, end='')
                c += 1
            else:
                print(elemento, end=' ')
                c += 1
        print()

def multiplicar_matrizes(m1, m2):
    '''Como a funcao cria_matriz_a_multiplicar garante que não haverá
    erro, essa função está inútil aqui em relação à verificação da 
    correspondência de tamanhos entre as colunas de m1 e as linhas de 
    m2, mas ela invoca a função imprime_matriz, que 'pretty prints' as
    matrizes a, b, a * b, m1, m2, e o resultado, m3.'''

    if sao_multiplicaveis(m1, m2) == True:
        imprime_matriz(multiplica_matrizes(m1, m2))
    else:
        print("Infelizmente as matrizes não são multiplicáveis.")

def multiplica_matrizes(m1, m2):
    assert len(m1[0]) == len(m2)
    m3, elemento_m3, soma = [], 0, 0
    m1_lin, m1_col, m2_lin, m2_col = 0, 0, 0, 0
    for linha in m1:
        m3.append([])
    for linha in m3:
        while elemento_m3 < len(m2[0]):
            while m1_col < len(m1[0]):
                soma += (
                    m1[m1_lin][m1_col] \
                  * m2[m2_lin][m2_col]
                        )
                m1_col += 1
                m2_lin += 1
            linha.append(soma)
            soma, m1_col, m2_lin = 0, 0, 0
            elemento_m3 += 1
            m2_col += 1
        elemento_m3, m2_col = 0, 0
        m1_lin += 1
    return m3

a = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [1,2,3]
    ]

b = [
        [1,2,3,4],
        [5,6,7,8],
        [9,1,2,3]
    ]

def main():
    print("\nMultiplicando variável a * b")
    print("\na =", a)
    imprime_matriz(a)
    print("\nb =", b)
    imprime_matriz(b)
    print()
    print("a * b =", multiplica_matrizes(a, b))
    multiplicar_matrizes(a, b)
    print("\nAgora, iremos multiplicar as matrizes: m1 * m2")
    print("A matriz resultante m3 terá as linhas de m1 e colunas de m2")
    print("\nDigite os valores de m1:")
    print("------------------------")
    m1 = cria_matriz()
    print("\nm2 terá a mesma quantidade de linhas\n            que m1 tem de colunas:", len(m1[0]))
    print("------------------------------------")
    m2 = cria_matriz_a_multiplicar(m1)
    print("\nVamos multipicar m1:")
    imprime_matriz(m1)
    print("\nE m2:")
    imprime_matriz(m2)
    print()
    print("m1 * m2 = m3")
    print("------------")
    multiplicar_matrizes(m1, m2)

main()