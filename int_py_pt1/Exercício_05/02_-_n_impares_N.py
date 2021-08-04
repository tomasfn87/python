def main():

    entrada = int(input("Digite o valor de n: "))
    saida = 1
    cont = 1

    while cont <= entrada:
        if saida % 2 != 0:
            print(saida)
            cont += 1
        saida += 1
    
main()