def criar_entradas(lista):
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
    return

def criar_dicionario(lista_chaves, lista_valores):
    dicionario = criar_entradas(lista_chaves)
    atribuir_valores(dicionario, lista_valores)
    return dicionario