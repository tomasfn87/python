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
            print('Insira o valor do elemento ', end='')
            print(cont_coluna, end='')
            print(' da linha ', end='')
            print(cont_linha, end='')
            print(': ', end='')
            linha.append(int(input()))
            cont_coluna += 1
        matriz.append(linha)
        cont_linha += 1
        
    return matriz

def cria_matriz():
    n_linhas = int(input('Insira o número de linhas: '))
    n_colunas = int(input('Insira o número de colunas: '))
    print()
    
    return valores_matriz(n_linhas, n_colunas)

def imprime_matriz():

    matriz = cria_matriz()

    print()
    print('===============')
    print(' A sua matriz: ')
    print('---------------')
    print()
    for linha in matriz:
        for elemento in linha:
            print(elemento, '\t', end='')
        print()
    print()
    print('---------------')

imprime_matriz()