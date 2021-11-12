class Listas:
    def criar_chaves(lista):
        dicionario = {}
        for i in lista:
            dicionario[i] = ""
        return dicionario

    def atribuir_valores(dicionario, lista, novo=False):
        assert len(dicionario) == len(lista)
        dicionario_final = dicionario
        if novo == True:
            dicionario_final = {}
        c = 0
        for i in dicionario:
            dicionario_final[i] = lista[c]
            c += 1
        return dicionario_final

    def criar_dicionario(lista_chaves, lista_valores):
        dicionario = Listas.criar_chaves(lista_chaves)
        Listas.atribuir_valores(dicionario, lista_valores)
        return dicionario

    def obter_chaves(dicionario):
        lista_chaves = []
        for i in dicionario:
            lista_chaves.append(i)
        return lista_chaves

    def obter_valores(dicionario):
        lista_valores = []
        for i in dicionario:
            lista_valores.append(dicionario[i])
        return lista_valores
    
    def sortDictsByKey(dict_arr, key, inv=False):
        # receives an array containing dictionaries that contain the informed key
        if Listas.dictsHaveKey(dict_arr, key) == False:
            return False
        sortedDictArr = dict_arr[:]
        values = []
        for d in dict_arr:
            values.append(d[key])
        for i in range(1, len(values)):
            for j in range(0, len(values) - i):
                if inv:
                    if values[j] < values[j+1]:
                        values[j], values[j+1] = values[j+1], values[j]
                        sortedDictArr[j], sortedDictArr[j+1] = \
                            sortedDictArr[j+1], sortedDictArr[j]
                else:
                    if values[j] > values[j+1]:
                        values[j], values[j+1] = values[j+1], values[j]
                        sortedDictArr[j], sortedDictArr[j+1] = \
                            sortedDictArr[j+1], sortedDictArr[j]
            i += 1
        return sortedDictArr
    
    def dictsHaveKey(dict_arr, key):
        # checks if all items in array containing dictionaries contrain the informed key
        for d in dict_arr:
            if key not in d.keys():
                return False
        return True
    
    def analisarListaDict(lista, chaves=[]):
        maiorItem = 0
        tamanhoAtual = 0
        for i in lista:
            allKeys = i.keys()
            if chaves in [[], "", {}, ()]:
                for c in allKeys:
                    tamanhoAtual += len(str(i[c]))
            else:
                for c in chaves:
                    tamanhoAtual += len(str(i[c]))
            if tamanhoAtual > maiorItem:
                maiorItem = tamanhoAtual
            tamanhoAtual = 0
        return maiorItem

    def checarListaListas(listaListas):
        if type(listaListas) != list:
            return False
        if len(listaListas) == 0:
            return False
        for i in listaListas:
            if type(i) !=  list:
                return False
        return True

    def unirListas(listaListas):
        if not Listas.checarListaListas(listaListas):
            return False
        elif len(listaListas) ==  1:
            return listaListas[0]
        listaUnica = listaListas[0][:]
        for i in range(1, len(listaListas)):
            listaUnica.extend(listaListas[i])
        return listaUnica
