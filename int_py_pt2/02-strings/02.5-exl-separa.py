def separa_w(string, separador=" "):
    #--> .strip() / .split()
    i_string, lista, i_lista = 0, [""], 0

    while i_string < len(string):
        if string[i_string] != separador:
            lista[i_lista] += string[i_string]
            i_string += 1
        else:
            if separador != " ":
                    lista.append("")
                    i_lista += 1
                    i_string += 1
            else:
                if lista[i_lista] != "":
                    lista.append("")
                    i_lista += 1
                    i_string += 1
                else:
                    i_string += 1 
    if separador == " ":
        if lista[-1] == "":
            del lista[-1]
    return lista

def separa_f(string, separador=" "):
    '''separa(string, ",") - deixar o segundo parâmetro em branco usa 
    " " e limpa os espaços em branco no começo e no início da string'''
    lista, i_lista = [""], 0

    for c in string:
        if c != separador:
            lista[i_lista] += c
        else:
            if separador != " ":
                    lista.append("")
                    i_lista += 1
            else:
                if lista[i_lista] != "":
                    lista.append("")
                    i_lista += 1

    if separador == " ":
        if lista[-1] == "":
            del lista[-1]

    return lista

if __name__ == "__main__":
    import sys
    separa(int(sys.argv[1]))