import sys
import time
import fixed_fibonacci_ite, fixed_fibonacci_rec

n = 20

def main():
    inicio = time.time()
    print(f'Elemento {n} da Sequência de Fibonacci: {fixed_fibonacci_ite.fixed_fibonacci_ite(n)}')
    print(f'Tempo de execução para o elemento {n} da sequência de Fibonacci (versão iterativa): {time.time() - inicio} segundos')
    print()
    inicio = time.time()
    print(f'Elemento {n} da Sequência de Fibonacci: {fixed_fibonacci_rec.fixed_fibonacci_rec(n)}')
    print(f'Tempo de execução para o elemento {n} da sequência de Fibonacci (versão recursiva): {time.time() - inicio} segundos')

if __name__ == '__main__':
    input = sys.argv
    if len(input) > 1:
        n = int(eval(input[1]))
        if n < 0:
            n *= -1
        main()
    else:
        print('Escreva um número n inteiro após o nome do arquivo; se n for negativo, o sinal será removido.')
