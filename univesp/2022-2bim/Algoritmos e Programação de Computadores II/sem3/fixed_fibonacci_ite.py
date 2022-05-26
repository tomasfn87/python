import sys

def fixed_fibonacci_ite(n):
    if type(n) == str:
        n = int(eval(n))
    elif type(n) == float:
        n = int(n)
    if n < 0:
        n *= -1
    return fib_ite(n)


def fib_ite(n):
    if n < 2:
        return n
    fib = 0
    a, b = 0, 1
    count = 1
    while count < n:
        fib = a + b
        a, b = b, fib
        count += 1
    return fib

if __name__ == '__main__':
    input = sys.argv
    if len(input) > 1:
        n = int(eval(input[1]))
        if n < 0:
            n *= -1
        print(f'Elemento {n} da sequência de Fibonacci: {fixed_fibonacci_ite(n)}')
    else:
        print('Escreva um número n inteiro após o nome do arquivo; se n for negativo, o sinal será removido.')