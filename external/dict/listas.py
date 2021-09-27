def criar_chaves(lista):
	dicionario = {}
	for i in lista:
		dicionario[i] = ""
	return dicionario

def atribuir_valores(dicionario, lista):
    assert len(dicionario) == len(lista)
    c = 0
    for i in dicionario:
        dicionario[i] = lista[c]
        c += 1
    return dicionario

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