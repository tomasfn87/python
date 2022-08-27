n = int(input("Insira quantos múltiplos serão contados:"))
if not n > 0:
    n = int(input("(n > 0) Insira quantos múltiplos serão contados:"))
i = int(input("Insira o primeiro número a ser verificado:"))
if not n > 0:
    n = int(input("(n > 0) Insira o primeiro número a ser verificado:"))
j = int(input("Insira o segundo número a ser verificado:"))
if not n > 0:
    n = int(input("(n > 0) Insira o segundo número a ser verificado:"))

mult_i = mult_j = 0

cont = 0
while cont < n:
    if mult_i == mult_j:
        print(mult_i)
        mult_i = mult_i + i
        mult_j = mult_j + j
    elif mult_i < mult_j:
        print(mult_i)
        mult_i = mult_i + i
    else:
        print(mult_j)
        mult_j = mult_j + j
    cont += 1
        