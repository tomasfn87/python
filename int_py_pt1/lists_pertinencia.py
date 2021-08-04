cor1 = ['marrom', 'roxo', 'violeta', 'cinza']
cor2 = ['marrom', 'roxo', 'violeta', 'rosa']

'''
print('marrom' in cor1)
print('cinza' in cor2)

if 'rosa' in cor2:
    print('Tem essa cor ein')
else:
    print('Tá sem no momento, parceiro')

if 'cinza' in cor2:
    print('Tem essa cor ein')
else:
    print('Tá sem no momento, parceiro')

print([1, 2] + [3, 4], '\n')
'''

cor2_len = len(cor2)
cor2_cont = 0
while cor2_len > cor2_cont:
    if cor2_cont == cor2_len - 1:
        cor2.append(cor1[cor2_cont])
        cor2_cont += 1
    else:
        cor2.append(cor1[cor2_cont])
        cor2_cont += 1
        print(cor2)
print()
print(cor2)

'''
Este trecho adiciona um a um os elementos da lista 'cor1' à lista 'cor2'. 
Não gerá cópia, modifica a lista 'cor2' original.
'''