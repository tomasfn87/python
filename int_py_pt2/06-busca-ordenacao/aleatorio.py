import random

def lista_aleatoria(n):
    aleatorio = random.randint
    lista_aleatoria = []

    for i in range(n):
        lista_aleatoria.append(aleatorio(1, n))
    return lista_aleatoria

def lista_quase_ordenada(n):
    lista_quase_ordenada = [x for x in range(n)]
    lista_quase_ordenada[n//10] = -500
    lista_quase_ordenada[n//2] = -150
    lista_quase_ordenada[n//4] = 1000
    lista_quase_ordenada[n//7] = 333
    return lista_quase_ordenada