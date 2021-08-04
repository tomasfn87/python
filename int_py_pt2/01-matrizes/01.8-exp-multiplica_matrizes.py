import sao_multiplicaveis
import imprimir

def multiplicar_matrizes(m1, m2):
    if sao_multiplicaveis.sao_multiplicaveis(m1, m2) == True:
        imprimir.imprime_matriz(multiplica_matrizes(m1, m2))
    else:
        print("As matrizes não são multiplicáveis =/")

def multiplica_matrizes(m1, m2):
    assert len(m1[0]) == len(m2)
    m3, elemento_m3, soma = [], 0, 0
    m1_lin, m1_col, m2_lin, m2_col = 0, 0, 0, 0
    for linha in m1:
        m3.append([])
        # n_linhas_m3 = n_linhas_m1
    for linha in m3:
        while elemento_m3 < len(m2[0]):
            # n_colunas_m3 = n_colunas_m2
            while m1_col < len(m1[0]):
                # linha_m1 * coluna_m2, percorre e soma
                soma += (
					m1[m1_lin][m1_col]\
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

a = [[1,2,3],[4,5,6],[7,8,9],[1,2,3]]
b = [[1,2,3,4],[5,6,7,8],[9,1,2,3]]
c = [[1],[2],[3]]