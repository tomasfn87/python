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

if __name__ == "__main__":
    import sys
    imprimir(int(sys.argv[1]))
