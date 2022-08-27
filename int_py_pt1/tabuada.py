print('Fill with empty spaces: ')
print()

linha = 1
coluna = 1
while linha <= 10:
    while coluna <= 10:
        print('{0: ^3}'.format(linha * coluna), end=' ')
        coluna += 1
    print()
    linha += 1
    coluna = 1

print()
print('Fill with dots: ')
print()


linha = 1
coluna = 1
while linha <= 10:
    while coluna <= 10:
        print('{0:.^3}'.format(linha * coluna), end=' ')
        coluna += 1
    print()
    linha += 1
    coluna = 1

print()
print('Fill with underscores: ')
print()

linha = 1
coluna = 1
while linha <= 10:
    while coluna <= 10:
        print('{0:_^3}'.format(linha * coluna), end=' ')
        coluna += 1
    print()
    linha += 1
    coluna = 1

print()
print('Fill with ~: ')
print()

linha = 1
coluna = 1
while linha <= 10:
    while coluna <= 10:
        print('{0:~^3}'.format(linha * coluna), end=' ')
        coluna += 1
    print()
    linha += 1
    coluna = 1
