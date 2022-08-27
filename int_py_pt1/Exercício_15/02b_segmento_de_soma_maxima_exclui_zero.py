def soma_elementos(x, y, lista):
# A função soma_elementos(x, y, lista) recebe o índice inicial 'x' e o
# índice final 'y' para que todos os elementos de 'lista' entre esses
# índices sejam somados um a um e retornados como um inteiro. 

    if len(lista) > 1: # Se o comprimento da lista for maior do que 1;
        soma = 0
        # Iniciando a 'soma' em '0' e adicionando elemento 'lista[x]'
        # e então percorrendo a lista com 'x + 1' até 'x < y'.

        while x < y:
            soma = soma + lista[x]    
            x += 1
            # Soma 1 em x para continuar a percorrer a lista somando
            # cada elemento.
        return soma
    elif len(lista) == 1: # Se o comprimento da lista for igual a 1,
        return lista[0]   # basta retornar o elemento lista[0];
    else:                 # Se o comprimento da lista for igual a zero,
        return 0          # a soma também será zero. 

def main():

    print(
    '\nEncontraremos o maior segmento de soma de uma lista com n elementos!'
    '\nVamos começar:\n'
    )

    n_input = 0
    while n_input <= 0:
        n_input = int(
            input(
        '1 - insira o número total de elementos da lista, n > 0: '
            )
        )
    print()

    lista = [] # Iniciei a lista vazia e adicionarei os elementos com o
               # comando 'lista.append()'.
    cont_input = 1 # Contador de itens a serem adicionados na lista, inicia
                   # em '1'.

    if n_input == 1:
        print(
            '2 - Insira', n_input,'número inteiro, positivo ou negativo: '
        )
    else:
        print(
            '2 - Insira', n_input,'números inteiros, positivos ou negativos: '
        )
    
    while len(lista) < n_input:
        print('2.', end='')            # , end='' e uma novo comando
        print(cont_input,'-', end=' ') # 'print' permitem eliminar o espaço
                                       # vazio após '2.'.
        if cont_input == n_input:
            item_lista = lista.append(int(input(
            # a variável item_lista usa a função list.append() para adicionar
            # os elementos digitados pelo usuário à lista 'lista'. 
                'insira o último número inteiro: '
                    )
                )
            )
        else:
            item_lista = lista.append(int(input('insira um número inteiro: ')))
        cont_input += 1
    
    c1 = 0 # Para começar no primeiro elemento da lista, iniciei c1 = 0
    c2 = 1 # e c2 = 1. Nesse caso, o valor inicial de c2 foi determinado 
           # por mim, e não pela linha c2 = c1 + 1, como abaixo, evitando
           # um cálculo desnecessário. 

    print('\nA soma total é', soma_elementos(0, len(lista), lista), end='')
    # A linha acima informa para o usuário a soma de todos os elementos
    # da lista.

    if len(lista) == 1:
        print('\nA lista contém apenas um elemento:', lista[0])
    else:
        print('.\nIremos encontrar o maior segmento de soma para você...')
    
        print()

        seg_soma = soma_elementos(0, 1, lista) 
        # A soma de todos os elementos da lista será comparado com os segmentos da
        # lista.
                        
        seg_soma_max = lista[0:len(lista)] 
        # A variável que armazena o segmento da lista que devemos mostrar para o
        # usuário.

        # As repetições encaixadas 'while' percorrem todos os segmentos de
        # 'lista' e os comparam, guardando o maior em 'seg_soma_max'.
        # As variáveis c1 e c2 são os contadores que percorrem os índices
        # de 'lista'. c2 é inicia sempre em (c1 + 1), iniciando em 0 e 1.
        while c1 != (len(lista) - 1) and c2 != len(lista):
            while c2 <= len(lista):
                if seg_soma < soma_elementos(c1, c2, lista):
                    seg_soma_max = lista[c1:c2]
                    seg_soma = soma_elementos(c1, c2, lista)
                c2 += 1
            c1 += 1
            c2 = c1 + 1 
            # Como mencionado acima, c2 é igual a c1 + 1.
            # No primeiro caso, c1 = 0 e c2 = 1.
        
        c3 = 0 
        # Contador para percorrer a lista verificando se algum dos 
        # elementos é maior do que a soma do maior segmento da lista.

        while c3 < len(lista):
            if seg_soma > lista[c3]:
                c3 += 1
            elif seg_soma <= lista[c3]:
                seg_soma_max = lista[c3:(c3 + 1)]
                c3 += 1

        if seg_soma_max == lista:
            # Quando não existirem ou existem apenas elementos negativos fracos:
            # - ou -
            # Existirem apenas elementos negativos:
            # - ou -
            # A maior soma é obtida somando todos os elementos da lista:

            print(
                'A lista completa é o maior segmento de soma da lista'
                ' fornecida: ', seg_soma_max, end=''
            )
            print(
                '.\nO maior segmento de soma continua sendo a soma total, que é igual'
                ' a', seg_soma, end=''
            )
        elif len(seg_soma_max) == 1:
            # Quando um elemento isolado  for maior do que a soma da lista toda.
            # Não foi pedido no exercício, portanto salvei uma nova versão do código. 
            print(
                'Um elemento isolado é maior do que qualquer segmento de soma'
                ' da lista fornecida: ', seg_soma_max[0], end=''
            )
            print(
                '.\nA lista fornecida foi', lista, end=''
            )
        else: 
            # Quando existirem elementos negativos fortes com os positivos:
            # - ou -
            # A maior soma é obtida a partir de um segmento da lista:

            print(
                'Este é o maior segmento de soma da lista fornecida: ',
                seg_soma_max, end=''
            )
            print('.\nA soma dos elementos desse segmento é', seg_soma, end='')
        print('.') 
                # O ponto final é útil em todos os casos, portanto está
                # fora da indentação. Não pulei linha pois o conteúdo está
                # ligado à saida dos condicionais 'if' e 'else' acima.
    
main()