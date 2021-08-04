def maximo(a, b, c):
    if a > b > c or a > c > b:
        return a
    elif b > a > c or b > c > a:
        return b
    elif c > a > b or c > b > a:
        return c
    elif a == b == c:
        return a

def test_maximo_3_1():
    maximo(1, 2, 3) == 3

def test_maximo_3_2():
    maximo(3, 2, 1) == 3

def test_maximo_3_3():
    maximo(10, 5, 3) == 10

def test_maximo_3_4():
    maximo(75, 100, 50) == 100

def test_maximo_3_5():
    maximo(4, 4, 4) == 4

def test_maximo_3_6():
    maximo(4, 2, 2) == 4

'''def main():

    print("Descubra qual é o maior entre 3 valores quaisquer:")
    x = int(input('\t{0:_^32}'.format('Insira o primeiro valor: ')))
    y = int(input('\t{0:_^32}'.format('Insira o primeiro valor: ')))
    z = int(input('\t{0:_^32}'.format('Insira o primeiro valor: ')))
    print('\n\t', '{0:_^28}'.format('O maior valor é'),':', maximo(x, y, z))

main()'''