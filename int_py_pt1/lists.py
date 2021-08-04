playlist_Nirvana = ['Heart-Shaped box', 'Aneurysm', 'Tourette\'s', 'Sappy', 'Dive', 'Breed', 'Territorial Pissings']
lis = [3, 4, 6, 7, 12, 17, 699, 701]
filme = ['O Sétimo Selo', 1957, 96, 'Ingmar Bergman', 'Sweden']

print(type(filme[0]))
print(type(filme[1]))
print(type(filme[2]))
print(type(filme[3]))
print(type(filme[4]))
print()

def checar_primo(x):
    if x == 0:
        return True
    elif x == 1:
        return False
    elif x == 2:
        return True
    elif x > 2:
        div = 2
        while x > div:
            while x % div != 0:
                div += 1
            if x > div:
                return False
        return True

limite = int(input('digite o limite máximo: '))
n = 2
while n < limite:
    if checar_primo(n):
        print(n, end=', ')
    n += 1