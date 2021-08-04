def menor_string(lista_de_strings):
    # menor string quer dizer anterior na ordem alfabética

    menor_string = ''
    for string in lista_de_strings:
        if menor_string == '' and string != '':
            menor_string = string
        elif string.lower() < menor_string.lower():
            menor_string = string
    return menor_string.capitalize()

def testa_menor_string(lista_de_str, resultado_esperado):
    if menor_string(lista_de_str) != resultado_esperado:
        return False
    else:
        return True

'''
Para implantar um teste:
------------------------

  I) criar uma varíavel com o nome teste_x, cujo conteúdo deverá ter
2 itens --> 1:

    1) uma lista, contendo nenhuma mas idealmente pelo menos duas
  strings;
    2) a string cujos elementos tem o menor valor de ord(), ou seja que
  vem primeiro na ordem alfabética, e, de uma forma geral, o resultado
  esperado da função, filtrado pelo método .capitalize() - ou
  simplesmente o resultado esperado com a primeira letra maiúscula.

  II) adicionar um elemento na variável testes seguindo o modelo --> 2:
testa_menor_string(teste_x[0], teste_x[1])

  Obs.: O teste só funciona com strings sem espaços antes ou depois, 
portanto idealmente você deve filtrar o input() do seu usuário através
do método .strip()
'''

teste_1 = (
    ["ana", "maria", "José", "Valdemar"],
     "Ana"
)

teste_2 = (
    ["Peterson", "José Carlos", "Daniel", "Eustáquio", "Muriel", "tiago"],
     "Daniel"
)

teste_3 = (
    ["Alaíde", "Tomás", "Margarida", "arlete", "brisa", "alice"],
     "Alaíde"  
)

'''
--> 1{
    teste_x = (
        ["str_1", "str_2"],
         "str_resultado_esperado.capitalize()"
    )
}
'''

testes = [
    testa_menor_string(teste_1[0], teste_1[1]),
    testa_menor_string(teste_2[0], teste_2[1]),
    testa_menor_string(teste_3[0], teste_3[1]) #,
    # --> 2{ 
    # testa_menor_string(teste_x[0], teste_x[1])
    # }
]

def executar_testes():
    for teste in testes:
        if teste == False:
            return print(
                "Um dos testes falhou. Existem correções a serem feitas."
            )
    print("Todos os testes deram certo.")

executar_testes()