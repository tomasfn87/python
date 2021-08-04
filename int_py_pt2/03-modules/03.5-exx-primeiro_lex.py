def primeiro_lex(lista):
    primeiro_lex = ''
    for string in lista:
        if primeiro_lex == '' and string != '':
            primeiro_lex = string
        elif string < primeiro_lex:
            primeiro_lex = string
    return primeiro_lex