import separa

def maior_palavra(string):
    palavras = separa.separa_f(string)
    maior_palavra, tamanho_maior_palavra = '', 0

    for p in palavras:
        if len(p) > tamanho_maior_palavra:
            tamanho_maior_palavra, maior_palavra = len(p), p
    return maior_palavra

if __name__ == "__main__":
    import sys
    maior_palavra(int(sys.argv[1]))