def n_primos(x):
    
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

    n = int(input('Insira o número a ser verificado: '))
    if not n > 0:
        n = int(input('\tRespeite (n > 0).  Insira novamente o número a ser verificado: '))
    
    print(n_primos(n))

main()