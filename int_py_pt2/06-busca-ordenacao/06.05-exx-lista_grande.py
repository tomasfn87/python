import random

def lista_aleatoria(n):
    aleatorio = random.randint
    lista_aleatoria = []

    for i in range(n):
        lista_aleatoria.append(aleatorio(1, n))
    return lista_aleatoria

def lista_quase_ordenada(self, n):
    lista = [x for x in range(n)]
    lista[n//10] = -500
    return lista