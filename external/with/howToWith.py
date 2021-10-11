import random
with open('scrap.book', 'a') as arquivo:
    arquivo.write(str(random.randint(100, 1000)) + "\n")