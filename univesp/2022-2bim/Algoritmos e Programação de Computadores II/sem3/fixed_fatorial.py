import sys

def fixed_fatorial(n):
    if type(n) == str:
        n = int(eval(n))
    elif type(n) == float:
        n = int(n)
    if n < 0:
        n *= -1
    return fat(n)

def fat(n):
    if n == 1:
        return 1
    else:
        return n * fat(n-1)
    
if __name__ == '__main__':
    input = sys.argv
    if len(input) > 1:
        n = int(eval(input[1]))
        if n < 0:
            n *= -1
        print(f'Fatorial de {n}: {fixed_fatorial(n)}')
    else:
        print('Escreva um número n inteiro após o nome do arquivo; se n for negativo, o sinal será removido.')