import random

def get_random_number_list(n):
    l = []
    for i in range(0, n):
        l.append(500)
    for i in range(0, n):
        l[i] = int(random.random() * l[i])
    return l