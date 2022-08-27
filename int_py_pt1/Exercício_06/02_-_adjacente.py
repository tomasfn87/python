def main():

    adjacente = False
    valor = int(input("Digite um número inteiro: "))
    valor0 = valor

    while valor0 != 0 and not adjacente:
        if (valor0 % 10) == ((valor0 // 10) % 10): # and valor0 != 0:
            adjacente = True
            alg_adj = valor0 % 10
        valor0 = (valor0 // 10)

    if adjacente == True:
        print("sim")
    else:
        print("não")

main()
