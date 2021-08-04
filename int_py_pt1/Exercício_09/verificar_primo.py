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

def test_checar_primo_1():
    assert checar_primo(2) == True

def test_checar_primo_2():
    assert checar_primo(4) == False

def test_checar_primo_3():
    assert checar_primo(5) == True

def test_checar_primo_4():
    assert checar_primo(9) == False

def test_checar_primo_4():
    assert checar_primo(11) == True

def main():
    n = int(input('Insira o número a ser verificado se é primo: '))
    while n >= 0:
        if checar_primo(n) == True:
            print('\t', n, 'é primo =)')
        if checar_primo(n) == False:
            print('\t', n, 'não é primo =|')
        n = int(input('\nInsira outro número a ser verificado: '))

main()