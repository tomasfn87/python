def main():

    entrada = int(input("Digite o valor de n: "))
    if entrada < 0:
        entrada = int(input("'n' deve obedecer a: 'n >= 0': "))

    fator = 1 #é '1' pois tanto 0! quanto 1! equivalem a 1. Quando o valor de entrada for 
    # menor que 2, basta replicar o valor de 'fator'. A multiplicação do fatorial inicia-se
    # em 2, portanto é o ponto  de partida para 2! em diante. 
    cont = 2 

    while cont <= entrada:
        fator = fator * cont #o valor de 'fator' será atualizado cada vez que 'cont' subir, 
        # carregando assim o seu novo valor adiante. 
        cont += 1 # essa variável subirá até ficar equivalente ao valor de entrada, desse 
        # modo, 'fator' será sempre 1 quando o valor de 'entrada' for menor do que 2. 
    print(fator) #abaixo de 2 o valor de 'n!' é sempre 1, portanto é só mostrar 'fator' sem
    # alterar. 

main()