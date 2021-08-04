def remove_repetidos(lista):
    cont1 = 0
    cont2 = 1

    if len(lista) > 1:
        while cont1 < len(lista):
            while cont2 < len(lista):
                if lista[cont1] == lista[cont2]:
                    del lista[cont2]
                else:
                    cont2 += 1
            cont1 += 1
            cont2 = cont1 + 1
        lista.sort()
    else:
        pass

    return lista