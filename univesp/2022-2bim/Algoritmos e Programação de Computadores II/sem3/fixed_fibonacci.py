import sys

def fixed_fibonacci(n):
    if type(n) == str:
        n = int(eval(n))
    elif type(n) == float:
        n = int(n)
    if n < 0:
        n *= -1
    return fib(n)

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    input = sys.argv
    if len(input) > 1:
        n = int(eval(input[1]))
        if n < 0:
            n *= -1
        print(f'Soma da sequência de Fibonacci de {n}: {fixed_fibonacci(n)}')
    else:
        print('Escreva um número n inteiro após o nome do arquivo; se n for negativo, o sinal será removido.')