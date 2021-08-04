def main():
    num = int(input("Digite um número inteiro: "))
    soma = 0

    while num != 0:
        soma = soma + num
        num = int(input("Digite um número inteiro: "))

    print("A soma é", soma)


#----------------------------------------------
main()
