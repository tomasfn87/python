def soma_elementos(x, y, lista):
    if len(lista) > 1:
        soma = 0
        while x < y:
            soma = soma + lista[x]
            x += 1
        return soma
    elif len(lista) == 1:
        return lista[0]
    else:
        return 0