def main():

    myCard = int(input("Digite o número do seu cartão de crédito: "))

    readCard = 1
    foundMyCard_list = False

    while readCard != 0 and not foundMyCard_list:
        readCard  = int(input("Dite o número do próximo cartão: "))
        if readCard == myCard:
            foundMyCard_list = True

    if  foundMyCard_list:
        print("Oba, meu cartão está na lista disgraça!")
    else:
        print("Tá aqui não (r)apá!")

main()
