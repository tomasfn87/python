'''def maiusculas(frase):
    maiusculas = ""
    for char in frase:
        if ord(char) >= 65 and ord(char) <= 90:
            maiusculas += char
    return maiusculas
'''
# conta quantos caracteres são maiúsculos em uma string
def maiusculas(frase):
    maiusculas = ""
    for char in frase:
        if 65 <= ord(char) <= 90:
            maiusculas += char
    return maiusculas