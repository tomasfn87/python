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

def testa_mais_curto():
    lista_mais_curtos = []
    testes  = \
    [
        ["    ana       ", "jOSé ", "aleSSandra", "Eustácio", "cAsSiAnO", "AlEf"],
        [" carla ", "ERIC", "TeobaldO", "Greta", "pérICles", "João", "Margarete"],
        ["Paula", "Maria", "Tuila", "Tássia", "Tadeu", "Tom"],
        ["Tiago", "  Amir", "Gandalf", "Lestat", "Anna ", "   Ganesh"]
    ]

    for lista in testes:
        lista_mais_curtos.append(mais_curto(lista))
    
    if lista_mais_curtos != ["Ana", "Eric", "Tom", "Amir"]:
        print("A sua função ainda não está funcionando bem...")
        return False
    else:
        print("A sua função está funcionando bem! Parabéns!")
        return True
        