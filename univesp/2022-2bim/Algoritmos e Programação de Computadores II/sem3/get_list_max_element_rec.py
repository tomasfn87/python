import time
import rand_num_list

def max_rec(l):
    if len(l) == 1:
        return l[0]
    if l[0] <= l[1]:
        l.pop(0)
    else:
        l.pop(1)
    return max_rec(l)

l1 = rand_num_list.get_random_number_list(998)

inicio = time.time()
print(max_rec(l1))
print(f'Encontrar o maior elemento usando minha função recursiva leva {time.time() - inicio} segundos')
print()
inicio = time.time()
print(max(l1))
print(f'Encontrar o maior elemento usando a função nativa "max()" leva {time.time() - inicio} segundos')
