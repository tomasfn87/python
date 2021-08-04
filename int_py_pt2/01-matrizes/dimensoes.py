def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    return (linhas, colunas)

if __name__ == "__main__":
    import sys
    dimensoes(int(sys.argv[1]))