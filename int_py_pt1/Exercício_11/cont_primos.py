def contar_primos(x):
    
    contPrimos = 0
    while x > 1:
        if checar_primo(x) == True:
            contPrimos += 1
            x -= 1
        else:
            x -= 1
    return contPrimos

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

def main(): 

    n = 0
    while not n == -1:
        print('\n* Digite -1 para encerrar o programa.\n')
        n = int(input('\tInsira o número até o qual será verificada a quantidade de primos: '))
        if n == -1:
            exit('\nObrigado por contar os números primos conosco. =)')
        elif not n > 0:
            n = int(input('\tespeite (n > 0).  Insira novamente o número a ser verificado: '))
        
        print('\n\tExistem', contar_primos(n),'números primos até', n, end='')
        print('.')
        if checar_primo(n) == True:
            if n - 1 == 2:
                print('\tO número', n,'também é primo, portanto', (contar_primos(n) - 1),'número primo abaixo de', n, end='')    
            else:
                print('\tO número', n,'também é primo, portanto são', (contar_primos(n) - 1),'números primos abaixo de', n, end='')
            print('.')
        else:
            print('\tO número', n,'não é primo.')

main()