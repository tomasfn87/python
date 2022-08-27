lista = []
while len(lista) == 0 or lista[-1] != 0:
    add_to_lista = lista.append(int(input('digite um número diferente de 0: ')))
    #print('digite 0 e aperte ENTER para somar os números da lista\ne imprimir a lista na ordem inversa.')
lista.sort(reverse = True)
print(lista)




    


    