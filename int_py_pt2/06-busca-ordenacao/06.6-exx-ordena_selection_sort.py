def ordena(lista):
    for i in range(len(lista) - 1):
        # i percorre os indices da lista

        indice_menor_valor = i
        '''Antes de iniciar o processo de ordenação, o índice (i) do 
        primeiro elemento da lista assumirá o valor de 
        indice_menor_valor'''

        for j in range(i+1, len(lista)):
            ''' j percorre os elementos restantes da lista, que ainda
            não foram ordenados, por isso inicia em i+1 (o próximo 
            elemento da lista) e vai até o fim da lista (len(lista))'''

            if lista[j] < lista[indice_menor_valor]:
                '''Caso seja encontrado um elemento com valor menor do
                que lista[indice_menor_valor], indice_menor_valor 
                receberá o valor de j.'''
                indice_menor_valor = j

        lista[i], lista[indice_menor_valor] = lista[indice_menor_valor], lista[i]
        '''Ao fim da lista, se não houver elemento com valor menor que
        lista[indice_menor_valor], lista[i], que é o índice do elemento
        que está sendo ordenado, trocará de valor com 
        lista[indice_menor_valor]'''
    
    return lista