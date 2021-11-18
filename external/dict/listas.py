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

        * if "inv" receives "True", the sorting will be reversed;

        * if "noCase" receives "True", the sorting will group letters
        ignoring upper and lower cases in a first moment, and then will
        take it into account again to group the same letters: first 
        upper case letters and the lower case letters.
        Example: "['A','b','C','a']" returns "['A','a','b','C']"
        (list.sort() would return "['A','C','a','b']");

        * if "targetArr" receives a valid argument, the function will
        check if it's a list and if its length is the same as "arr": 
        if the result is True, the function will sort the second list
        based on the first list, returning a copy of the second list,
        that may even end up unordered, depending on the correlation 
        between "arr" and "targetArr" - the problem is solved if the
        lists are copies of each other slightly modified, for example.
        '''
        if targetArr:
            if type(targetArr) != list or len(arr) != len(targetArr):
                return False
            sortArr = targetArr[:]
        else:
            sortArr = arr[:]
        refArr = arr[:]
        for i in range(1, len(refArr)):
            for j in range(0, len(refArr) - i):
                if noCase:
                    if refArr[j].lower() == refArr[j+1].lower()\
                        and refArr[j] > refArr[j+1]:
                        refArr[j], refArr[j+1] = refArr[j+1], refArr[j]
                        sortArr[j], sortArr[j+1] = sortArr[j+1],sortArr[j]
                    elif refArr[j].lower() > refArr[j+1].lower():
                        refArr[j], refArr[j+1] = refArr[j+1], refArr[j]
                        sortArr[j], sortArr[j+1] = sortArr[j+1], sortArr[j]
                else:
                    if refArr[j] > refArr[j+1]:
                        refArr[j], refArr[j+1] = refArr[j+1], refArr[j]
                        sortArr[j], sortArr[j+1] = sortArr[j+1], sortArr[j]
            i += 1
        if inv:
            sortArr.reverse()
        return sortArr

    def sortArrListCaseIns(arrListEntry, inv=0, noCase=0, targetArrList=0):
        '''Similar to "Listas.sortArrCaseIns()", but instead of sorting
        a single array, it will sort an array of arrays.
        * CaseIns = Case Insensitive'''
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
        # informed key and sort the dictionary list based on each
        # item's value for the specified key
        if not Listas.dictsHaveKey(dictArr, key):
            return False
        sortedDictArr = dictArr[:]
        values = []
        for d in dictArr:
            values.append(d[key])
        sortedDictArr = Listas.sortArrCaseIns(values, inv, noCase, sortedDictArr)
        return sortedDictArr

    def dictsHaveKey(dictArr, key):
        # checks if all items in a dictionary array contain the
        # informed key
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
        elif len(listaListas) == 1:
            return listaListas[0]
        listaUnica = listaListas[0][:]
        for i in range(1, len(listaListas)):
            listaUnica.extend(listaListas[i])
        return listaUnica
