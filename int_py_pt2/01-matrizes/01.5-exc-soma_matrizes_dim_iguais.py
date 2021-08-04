def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    return (linhas, colunas)

def soma_matrizes(m1, m2):
    
    soma_matrizes = []
    linha_m1 = 0
    linha_m2 = 0
    coluna_m2 = 0

    if dimensoes(m1) != dimensoes(m2):
        return False
    else:
        for linha in m1:
            soma_matrizes.append([])
            for elemento in linha:
                soma_matrizes[linha_m1].append(
                    elemento + m2[linha_m2][coluna_m2]
                )
                coluna_m2 += 1
            coluna_m2 = 0
            linha_m1 += 1
            linha_m2 += 1

        return soma_matrizes