def fatorial(x):
    if x < 0:
        return 0
    i = fat = 1
    while i <= x:
        fat = fat * i
        i += 1
    return fat

def main():
    n = int(input("Digite um número inteiro, (n >= 0): "))
    while n >= 0:
        print(fatorial(n))
        n = int(input("Digite outro número inteiro: "))
    
main()