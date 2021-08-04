'''frutas_que_gosto = ['abacaxi', 'manga', 'pêssego', 'uva', 'morango', 'acerola', 'amora']

for fruta in frutas_que_gosto: 
    print('Eu sempre como ' + fruta)
print()
for fruta in frutas_que_gosto: 
    print('Eu gosto de ' + fruta)
'''

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
primos_1 = primos.copy()  #Dessa forma, 'primos_1' e 'primos_2' serão cópias independentes e 
primos_2 = primos.copy()  #não compartilharão os mesmos valores que 'primos'.
primos_3 = primos.copy()

'''
primos_1 = primos #Dessa forma as listas 'primo', 'primo_1' e 'primo_2' serão interligadas
primos_2 = primos #e compartilharãoos mesmos valores.
'''

'''clone manual:
def clone(lista):
    clone = []
    for objeto in lista:
        clone.append(objeto)
    return clone

    O fatiamento lista[:] já cria uma nova lista, facilitando o processo.
'''


print('lista 1: ', primos_1)
print('lista 2: ', primos_2)
print('lista 3: ', primos_3)
print()

for i in range(0, 3, 1):
    primos_1[i] = primos_1[i]**2
print(primos_1, '\n')

for i in range(3, 6, 1):
    primos_2[i] = primos_2[i]**2
print(primos_2, '\n')

for i in range(6, len(primos_3), 1):
    primos_3[i] = primos_3[i]**2
print(primos_3, '\n')

print()
print('lista 1: ', primos_1)
print('lista 2: ', primos_2)
print('lista 3: ', primos_3)
print('lista original: ', primos)
print()

'''for x in primos:
    print(x**2)
print()

for i in range(fim):
    COMANDO é assim que se faz!
for i in range(len(lista)): <- Exemplo de fim típico.
    COMANDO é assim que se faz!
for i in range(inicio, fim):
    COMANDO é assim que se faz!
for i in range(incio, fim, passo):
    COMANDO é assim que se faz!

print('\n\tNo código, valores ajustados ao que se deseja ver na tela: \n')
for i in range(36):
    print(i, end=', ')
print('\n')
for i in range(35, 96):
    print(i, end=', ')
print('\n')
for i in range(35, 351, 5):
    print(i, end=', ')
print('\n')
for i in range(350, 34, -5):
    print(i, end=', ')

print('\n\n\tNo código, valores que se deseja ver na tela, porém a indexação é iniciada em 0: \n')
for i in range(35):
    print(i, end=', ')
print('\n')
for i in range(35, 95):
    print(i, end=', ')
print('\n')
for i in range(35, 350, 5):
    print(i, end=', ')
print('\n')
for i in range(350, 35, -5):
    print(i, end=', ')

intervalo001 = range(10, 21, 1)
for i in intervalo001:
    print(i)'''