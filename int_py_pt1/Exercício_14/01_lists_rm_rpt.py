def remove_repetidos(lista):
    cont1 = 0
    cont2 = 1

    print('original: ',  lista)

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

def main():
    ent_lista = [1, 2, 3, 8, 5, 6, 7, 8, 7, 4, 2, 4, 2]
    remove_repetidos(ent_lista)
    print('sem itens repetidos e ordenada: ', ent_lista)

main()