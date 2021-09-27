def criar_chaves(lista):
	dicionario = {}
	for i in lista:
		dicionario[i] = ""
	return dicionario

def atribuir_valores(dicionario, lista, novo=False):
    assert len(dicionario) == len(lista)
    if novo == True:
        dicionario_final = {}
    elif novo == False:
        dicionario_final = dicionario
    c = 0
    for i in dicionario:
        dicionario_final[i] = lista[c]
        c += 1
    return dicionario_final

def criar_dicionario(lista_chaves, lista_valores):
    dicionario = criar_chaves(lista_chaves)
    atribuir_valores(dicionario, lista_valores)
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