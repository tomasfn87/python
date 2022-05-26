import time
import rand_num_list

def sum_list_items(l):
    if len(l) == 1:
        return l[0]
    else:
        l[-2] += l[-1]
        l.pop(-1)
    return sum_list_items(l)

l1 = rand_num_list.get_random_number_list(998)

inicio = time.time()
print(sum_list_items(l1))
print(f'Minha função recursiva que soma os elementos de uma lista leva {time.time() - inicio} segundos')
print()
inicio = time.time()
print(sum(l1))
print(f'A função nativa "sum()" leva {time.time() - inicio} segundos')
