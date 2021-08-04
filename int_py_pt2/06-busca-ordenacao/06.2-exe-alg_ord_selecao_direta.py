class Ordenar:
    def selecao_direta(self, lista): # direct sort

        fim = len(lista) 

        for i in range(fim - 1):
            # Inicialmente, o menor elemento já visto é o i-ésimo
            posicao_do_minimo = i

            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j
            
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
            
            '''
            Coloca o menor elemento encontrado no início da sub-lista.
            Para isso, troca de lugar os elementos nas posições i e 
            posicao_do_minimo.
            '''
        return lista

    def bolha(self, lista): # bubble sort

        fim = len(lista)

        for i in range(fim-1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista
    
    def bolha_curta(self, lista):

        fim = len(lista)

        for i in range(fim-1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
            if not trocou:
        return lista

    def insertion(self, arr):
        
        end = len(arr)

        for i in range(1, end):

            key = arr[i]
            
            j = i - 1

            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        return arr
        
                    

