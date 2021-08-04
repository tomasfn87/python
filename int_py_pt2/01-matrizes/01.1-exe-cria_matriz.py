def cria_matriz(num_linhas, num_colunas, valor):
    ''' (int, int, valor) -> matriz (lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas
    colunas em que cada elemento é igual ao valor dado.'''

    matriz  = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(valor)
        
        matriz.append(linha)
    
    return matriz