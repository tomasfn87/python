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

    def sortArrCaseIns(arr, inv=0, noCase=0):
        sortedArr = arr[:]
        for i in range(1, len(sortedArr)):
            for j in range(0, len(sortedArr) - i):
                if noCase:
                    if sortedArr[j].lower() == sortedArr[j+1].lower()\
                        and sortedArr[j] > sortedArr[j+1]:
                        sortedArr[j], sortedArr[j+1] =\
                            sortedArr[j+1],sortedArr[j]
                    elif sortedArr[j].lower() > sortedArr[j+1].lower():
                        sortedArr[j], sortedArr[j+1] =\
                            sortedArr[j+1], sortedArr[j]
                else:
                    if sortedArr[j] > sortedArr[j+1]:
                        sortedArr[j], sortedArr[j+1] =\
                            sortedArr[j+1], sortedArr[j]
            i += 1
        if inv:
            sortedArr.reverse()
        return sortedArr

    def sortDictsByKey(dictArr, key, inv=0, noCase=0):
        # receives an array containing dictionaries that contain the
        # informed key
        if not Listas.dictsHaveKey(dictArr, key):
            return False
        sortedDictArr = dictArr[:]
        values = []
        for d in dictArr:
            values.append(d[key])
        for i in range(1, len(values)):
            for j in range(0, len(values) - i):
                if noCase:
                    if values[j].lower() == values[j+1].lower()\
                        and values[j] > values[j+1]:
                        values[j], values[j+1] = values[j+1], values[j]
                        sortedDictArr[j], sortedDictArr[j+1] =\
                            sortedDictArr[j+1], sortedDictArr[j]
                    elif values[j].lower() > values[j+1].lower():
                        values[j], values[j+1] = values[j+1], values[j]
                        sortedDictArr[j], sortedDictArr[j+1] =\
                            sortedDictArr[j+1], sortedDictArr[j]
                else:
                    if values[j] > values[j+1]:
                        values[j], values[j+1] = values[j+1], values[j]
                        sortedDictArr[j], sortedDictArr[j+1] =\
                            sortedDictArr[j+1], sortedDictArr[j]
            i += 1
        if inv:
            sortedDictArr.reverse()
        return sortedDictArr

    def dictsHaveKey(dictArr, key):
        # checks if all items in array containing dictionaries contain
        # the informed key
        for d in dictArr:
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
