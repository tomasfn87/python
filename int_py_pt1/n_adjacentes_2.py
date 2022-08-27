def main():

    adjacente = 0
    valor = int(input("Digite o número para verificar se ele possui algarismos adjacentes, mostras quais são e quantas vezes aparecem: "))
    print()
    valor0 = valor

    while valor0 != 0:
        if (valor0 % 10) == ((valor0 // 10) % 10): #and valor0 != 0:
            adjacente += 1
            alg_adj = valor0 % 10
            print(" - Algarismo adjacente", adjacente,"=", alg_adj)
            print()
        valor0 = (valor0 // 10)

    if adjacente > 0:
        if adjacente == 1:
            print("O número", valor, "contém", adjacente, "algarismo adjacente. :)")
        else:
            print("O número", valor, "contém", adjacente, "algarismos adjacentes. :D")
    else:
        print("O número", valor, "não contém algarismos adjacentes. :|")

main()
