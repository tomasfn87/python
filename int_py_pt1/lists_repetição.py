list1 = [3, 2, 1]
list1_times3 = 3 *  list1
print(list1_times3)
print()

list2 = list1.copy()

for i in list2:
    print(i**2)

print()

#para deletar itens ou um treco da lista:
lista1 = [10, 100, 1000, 10000, 100000]
print(lista1)

del lista1[0:3]
'''# The line above produces the same output than the lines below:
del lista1[0]
del lista1[1]
del lista1[2]
'''

print(lista1)
