def menor_nome(lista_de_palavras):
    menor_nome = ''
    for dado in lista_de_palavras:
        nome = dado.strip().capitalize()
        if len(menor_nome) == 0 and len(nome) != 0:
            menor_nome = nome
        elif len(nome) > 0:
            if len(nome) < len(menor_nome):
                menor_nome = nome
    return menor_nome