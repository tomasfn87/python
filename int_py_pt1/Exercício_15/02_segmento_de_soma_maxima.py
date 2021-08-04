def soma_elementos(x, y, lista):
# A função soma_elementos(x, y, lista) recebe o elemento inicial 'x' e o
# elemento final 'y' a serem somados um a um da lista 'lista'.

    if len(lista) > 1: # Se o comprimento da lista for maior do que 1;
        soma = 0
        while x < y:
            soma = soma + lista[x] # Iniciando a 'soma' em '0' e adicionando 
            # elemento 'lista[x]' e então percorrendo a lista com 'x + 1' até
            # 'x < y'
            x += 1
            # Soma 1 em x para continuar a percorrer a lista somando cada 
            # elemento.
        return soma
    elif len(lista) == 1: # Se o comprimento da lista for igual a 1,
        return lista[0] # basta retornar o primeiro elemento da lista[0]
    else: # Se o comprimento da lista for igual a zero,
        return 0 # a soma também será zero. 

def main():
# A função principal do programa. Usei o nome padrão, 'main'. Poderia muito
# bem ser 'segmento_de_soma_máxima()'. Poderia trocar os 'print' por 'return'
# transformar 'main' em uma função que retorna o segmento de soma máxima ao
# invés de imprimir a soma máxima para o usuário, como faz esse programa.
# Esse programa tem um foco, portanto front-end: o usuário lê na tela a info.

    print(
    '\nEncontraremos o maior segmento de soma de uma lista com n elementos!'
    '\nVamos começar:\n'
    )

    n_input = int(
        input(
    '1 - insira o número total de elementos da lista, n > 0: '
        )
    )
    if n_input <= 0:
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
    print('2 - Insira', n_input,'números inteiros, positivos ou negativos: ')
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
    
    seg_soma = soma_elementos(0, len(lista), lista) 
    # A soma de todos os elementos da lista será comparado com os segmentos da
    # lista.
                    
    seg_soma_max = lista[0:len(lista)] 
    # A variável que armazena o segmento da lista que devemos mostrar para o
    # usuário.

    print('\nA soma total é', seg_soma, end='')
    # A linha acima informa para o usuário a soma de todos os elementos da
    # lista.
    print('.\nIremos encontrar o maior segmento de soma para você...')
    print()

    c1 = 0 # Para começar no primeiro elemento da lista, inicia-se em 'c1 =0'
    c2 = 1 # e  'c2 = 1'. Nesse caso, o valor inicial de c2 foi determinado 
           # por mim, e não pela linha 'c2 = c1 + 1', como abaixo, evitando
           # um cálculo desnecessário. 

    # As repetições encaixadas 'while' percorrem todos os segmentos de
    # 'lista' e os comparam, guardando o maior em 'seg_soma_max'.
    # As variáveis c1 e c2 são os contadores que percorrem os índices de
    # 'lista'. c2 é inicia sempre em (c1 + 1), iniciando em 0 e 1.
    while c1 != (len(lista) - 1) and c2 != len(lista):
        while c2 <= len(lista):
            if seg_soma < soma_elementos(c1, c2, lista):
                seg_soma_max = lista[c1:c2]
                seg_soma = soma_elementos(c1, c2, lista)
            c2 += 1
        c1 += 1
        c2 = c1 + 1 # Como mencionado acima, c2 é sempre igual a c1 + 1.
                    # No primeiro caso, c1 = 0 e c2 = 1, conforme escrito.
    
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
    else: 
        # Quando existirem elementos negativos fortes:
        # - ou -
        # A maior soma é obtida a partir de um segmento da lista:
        print(
            'Este é o maior segmento de soma da lista fornecida: ',
            seg_soma_max, end=''
        )
        print('.\nA soma dos elementos desse segmento é', seg_soma, end='')
    print('.') # O ponto final é útil em todos os casos, portanto está
               # fora da indentação. Não pulei linha pois o conteúdo está
               # ligado à saida dos condicionais 'if' e 'else' acima.

main() # Chama a função principal 'main' - roda o programa