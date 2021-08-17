def insertion_sort(lista):

        fim = len(lista)

        for i in range(1, fim):

            key = lista[i]

            j = i - 1
            while j >= 0 and key < lista[j]:
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = key
        return lista