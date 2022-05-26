import sys

def fixed_fibonacci_rec(n):
    if type(n) == str:
        n = int(eval(n))
    elif type(n) == float:
        n = int(n)
    if n < 0:
        n *= -1
    return fib_rec(n)

def fib_rec(n):
    if n < 2:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)

if __name__ == '__main__':
    input = sys.argv
    if len(input) > 1:
        n = int(eval(input[1]))
        if n < 0:
            n *= -1
        print(f'Elemento {n} da sequência de Fibonacci: {fixed_fibonacci_rec(n)}')
    else:
        print('Escreva um número n inteiro após o nome do arquivo; se n for negativo, o sinal será removido.')