def mais_curto(lista_de_palavras):
    menor_nome = ''
    for dado in lista_de_palavras:
        nome = dado.strip().capitalize()
        if len(menor_nome) == 0 and len(nome) != 0:
            menor_nome = nome
        elif len(nome) > 0:
            if len(nome) < len(menor_nome):
                menor_nome = nome
    return menor_nome

def mais_longo(lista_de_palavras):
    maior_nome = ''
    for dado in lista_de_palavras:
        nome = dado.strip().capitalize()
        if len(maior_nome) == 0 and len(nome) != 0:
            maior_nome = nome
        elif len(nome) > 0:
            if len(nome) > len(maior_nome):
                maior_nome = nome
    return maior_nome

print(
      'O mais curto é ' + mais_curto(lista_de_nomes)
    + ' e o mais longo é ' + mais_longo(lista_de_nomes) + '.'
    )