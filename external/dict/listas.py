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

    def sortArrCaseIns(arr, inv=0, noCase=0, targetArr=[]):
        '''This function uses Bubble Sort to sort a list ("arr"):

        * if inv receives True, the sorting will be reversed;

        * if noCase receives True, the sorting will group letters 
            ignoring upper and lower cases in a first moment, and
            then take it into account again to group the same letters:
            first upper case letters and the lower case letters.
            Example: "AbCa" returns "AabC"
            (list.sort() would return "ACab")
        
        * if "targetArr" receives a valid argument, the function will
        check if it's a list and if its length is the same as "arr": 
        if the result is True, the function will sort the second list
        based on the first list, returning a copy of the second list,
        that may even end up unordered, depending on the correlation 
        between "arr" and "target". This functionality was designed to
        be used directly by "Listas.sortArrListCaseIns()", which does
        basically the same thing, but instead of receiving two arrays 
        ("arr", "targetArr"), it receives two list of arrays
        ("arrList", "targetArrList").

        * "Listas.sortArrListCaseIns()" itself was designed to take
        advantage of "Listas.sortArrCaseIns()"'s "targetArr" parameter
        and remove the Bubble Sort algorithm from "Listas.sortDictsByKey()"
        '''
        if targetArr:
            if type(targetArr) != list or len(arr) != len(targetArr):
                return False
            sortedArr = targetArr[:]
        else:
            sortedArr = arr[:]
        refArr = arr[:]
        for i in range(1, len(arr)):
            for j in range(0, len(arr) - i):
                if noCase:
                    if refArr[j].lower() == refArr[j+1].lower()\
                        and refArr[j] > refArr[j+1]:
                        refArr[j], refArr[j+1] =\
                            refArr[j+1], refArr[j]
                        sortedArr[j], sortedArr[j+1] =\
                            sortedArr[j+1],sortedArr[j]
                    elif refArr[j].lower() > refArr[j+1].lower():
                        refArr[j], refArr[j+1] =\
                            refArr[j+1], refArr[j]
                        sortedArr[j], sortedArr[j+1] =\
                            sortedArr[j+1], sortedArr[j]
                else:
                    if refArr[j] > refArr[j+1]:
                        refArr[j], refArr[j+1] =\
                            refArr[j+1], refArr[j]
                        sortedArr[j], sortedArr[j+1] =\
                            sortedArr[j+1], sortedArr[j]
            i += 1
        if inv:
            sortedArr.reverse()
        return sortedArr

    def sortArrListCaseIns(arrListEntry, inv=0, noCase=0, targetArrList=0):
        if not Listas.checarListaListas(arrListEntry):
            return False
        arrList = []
        if targetArrList:
            if len(arrListEntry) != len(targetArrList):
                return False
            for i in range(0, len(arrListEntry)):
                arrList.append(
                    Listas.sortArrCaseIns(arrListEntry[i], inv, noCase, targetArrList[i])
                )
        else:
            for a in arrListEntry:
                arrList.append(Listas.sortArrCaseIns(a, inv, noCase))
        return arrList

    def sortDictArrByKey(dictArr, key, inv=0, noCase=0):
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

    def analyseLongestValueInDictList(lista, chaves=[]):
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
