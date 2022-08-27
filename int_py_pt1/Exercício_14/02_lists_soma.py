def soma_elementos(lista):
    if len(lista) > 1:
        soma = 0
        cont = 0
        while cont < len(lista):
            soma = soma + int(lista[cont])
            cont += 1
        return soma
    else:
        if len(lista) == 1:
            algarismo = lista[0]
            return algarismo
        else: 
            return lista