def main():
    entrada = int(input("Digite um número inteiro: "))
    if entrada <= 0:
        entrada = int(input("Digite um número inteiro (n > 0): "))

    valor = entrada
    sub = 1
    if valor == 2:
        print("primo")
    elif valor == 1:
        print("não primo")
    elif valor > 2:
        while (valor % (1 + sub)) != 0 and ((valor - sub)  > 1):
            sub += 1 
        if (valor - sub) == 1:
            print("primo")
        else:
            print("não primo")
    else:
        print("não primo")
main()