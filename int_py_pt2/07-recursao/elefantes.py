def incomodam(n, ready=False, texto=""):
    if ready == False:
        if n < 1:
            return incomodam(n, True)
        else:
            texto = incomodam(0)
            for i in range(0, n):
                texto += ("incomodam ")
            return incomodam(n, True, texto)
    else:
        return texto

def elefantes(n, ready=False, versos=incomodam(0)):
    if ready == False:
        if n < 1:
            return elefantes(n, True)
        else:
            for i in range(1, n + 1):
                if i == 1:
                    versos += "Um elefante incomoda muita gente..."
                else:
                    versos += "\n" + str(i) + " elefantes " \
                              + incomodam(i) + "muito mais!"
                    if i == n:
                        break
                    else:
                        versos += "\n" + str(i) + " elefantes " \
                                  + incomodam(1) + "muita gente..."
            return elefantes(n, True, versos)
    else:
        return versos

def main():
    run = 1
    while run == True:
        n_elefantes = int(input("Insira o número de elefantes: "))
        if n_elefantes == -1:
            break
        elif n_elefantes == 0:
            pass
        else:
            print()
            print(elefantes(n_elefantes))
        print("\n-1 para sair\n")

main()