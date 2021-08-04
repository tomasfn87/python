def conta_letras(frase, contar="vogais"):
    if contar == "vogais":
        return conta_vogais(frase)
    elif contar == "consoantes":
        return conta_consoantes(frase)
    '''
    elif contar != "vogais" and contar != "consoantes":
        print("Como segundo parâmetro opcional, insira uma das strings abaixo, explicitamente (com '' ou \"\"):\n1)'vogais'\n2)\"vogais\"\n3)'consoantes'\n4)\"consoantes\"\n\tou\n5) digite apenas a frase para usar o parâmetro 'vogais'.")
    '''

def conta_vogais(frase):
    n_vogais = 0
    vogais_Aa_ord_index = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]
    for c in frase:
        if ord(c) in vogais_Aa_ord_index:
            n_vogais += 1
    return n_vogais

def conta_consoantes(frase):
    n_consoantes = 0
    consoantes_Bb_ord_index = [66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78,\
        80, 81, 82, 83, 84, 86, 87, 88, 89, 98, 99, 100, 102, 103, 104, 106,\
        107, 108, 109, 110, 112, 113, 114, 115, 116, 118, 119, 120, 121]
    for c in frase:
        if ord(c) in consoantes_Bb_ord_index:
            n_consoantes += 1
    return n_consoantes

'''
ord = o índice que permite a ORDenação alfabética dos caracteres,
segundo a tabela ASCII.

print(ord("a"), ord("b"), ord("c"), ord("A"), ord("B"), ord("C"), ord("Ã"), ord("Â"), ord("Á"), ord("À"))
'''