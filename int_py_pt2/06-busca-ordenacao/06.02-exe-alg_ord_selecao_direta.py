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
    
    def merge_sort(lista):
        if len(lista) <= 1:
            return lista
        
        meio = len(lista) // 2

        lado_esquerdo = merge_sort(lista[:meio])
        lado_direito = merge_sort(lista[meio:])

        return merge(lado_esquerdo, lado_direito)

    def merge(lado_esquerdo, lado_direito):
        if not lado_esquerdo:
            return lado_direito
        
        if not lado_direito:
            return lado_esquerdo
        
        if lado_esquerdo[0] < lado_direito[0]:
            return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)
        
        return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])
        
                    

