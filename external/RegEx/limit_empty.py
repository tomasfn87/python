def limit_empty(string):
    espaco = True
    string_limpa = ''
    for i in string:
        if i == ' ':
            if espaco:
                string_limpa += i
                espaco = False
        else:
            string_limpa += i
            espaco = True
    return string_limpa.strip()   