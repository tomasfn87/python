import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e 
    devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma 
    lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input(
        "Digite o texto " + str(i) +" (aperte enter para sair):"
            )
    while texto:
        textos.append(texto)
        i += 1
        texto = input(
            "Digite o texto " + str(i) +" (aperte enter para sair):"
                )
    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas 
    dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases 
    dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras 
    dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de 
    palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de 
    palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)

#======================================================================

'''
 6 itens são necessários para calcular a assinatura do texto:
   a) - tamanho médio de palavra - soma tamanho palavras / # total 
   palavras

   b) - relação type-token (pal. diferentes / total palavras)

   c) - razão Hapax Legomana (pal. únicas / total palavras)

   d) - tamanho médio de sentença (soma caracteres todas sentenças / #
   de sentenças)
   tamanho_medio = soma_caracteres_total / total_sentenças 

   e) - complexidade de sentença - # total de frases / número (total)
   de sentenças
   complexidade_sentenca = total_frases / total_sentenças

   f) - tamanho médio de frase é a: 
   soma # de caracteres em cada frase / # frases no texto

 Elementos necessários:
    - tamanho palavras
    - número total de palavras
    - número total de palavras únicas
    - soma caracteres do texto todo
    - numero total de sentenças
    - número total de frases
    - caracteres por frase
 '''

# 1) Acredito que deve-se começar por esse item;

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a 
    assinatura do texto.'''
    assinatura_do_texto = [
        assinatura_1_tamanho_medio_palavras(texto),
        assinatura_2_relacao_type_token(texto),
        assinatura_3_razao_hapax_legomana(texto),
        assinatura_4_tamanho_medio_sentenca(texto),
        assinatura_5_complexidade_de_sentenca(texto),
        assinatura_6_tamanho_medio_de_frase(texto)
    ]
    return assinatura_do_texto
        

# 1.1) Criarei diferentes funções para facilitar a implementação do 
# programa.

def total_sentencas(texto): # OK!
    return len(separa_sentencas(texto))
    
def total_frases(texto):
    n_frases_por_sentenca = 0 # Será adiciona a total_frases e
    # e reinicializado a cada iteração de for;
    percorre_sent = 0 # Usado para percorrer os elementos 
                      # de cada sentença;
    total_frases = 0 # A cada iteração de for, recebe a quantidade
                     # de frases de cada sentença.
    lista_sentencas = separa_sentencas(texto)
    for sentenca in lista_sentencas:
        n_frases_por_sentenca =\
        len(separa_frases(lista_sentencas[percorre_sent]))
        total_frases = total_frases + n_frases_por_sentenca
        percorre_sent += 1
        n_frases_por_sentenca = 0
    return total_frases

def total_caracteres_com_espacos(texto): # OK! 
    return len(texto)

def total_caracteres_sem_espacos(texto):
    espacos_vazios = 0
    for caracter in texto:
        if caracter == ' ':
            espacos_vazios += 1
        else:
            pass
    return len(texto) - espacos_vazios

def total_caracteres_sem_espacos_e_sinais(texto):
    '''A função quebra o texto em itens de uma lista, removendo os
    sinais de pontuação do texto para então fazer a contagem dos 
    caracteres, ignorando espaços vazios. 
    Sinais removidos: ,:;.!?
    '''
    texto = re.split(r'[,:;.!?]+', texto)
    total_caracteres = 0
    espacos_vazios = 0
    percorre_caracteres = 0
    for frase in texto:
        if frase == '':
            del frase
        else:
            while percorre_caracteres < len(frase):
                if frase[percorre_caracteres] == ' ':
                    espacos_vazios += 1
                else:
                    pass
                percorre_caracteres += 1
            total_caracteres += len(frase) - espacos_vazios
            percorre_caracteres = 0
            espacos_vazios = 0
    return total_caracteres

def total_palavras(texto): # OK!
    return len(separa_palavras(texto))
   
def tamanho_palavra(dado_entre_espacos):
    '''Conta o número de caractares do dado entre espaços, para isolar
    o conteúdo desejado, as palavras, sem contabilizar os itens da
    lista sinais.'''

    sinais = ['.', ',', '!', '?', ':', ';', '"', '\'', '(', ')']
    tamanho_palavra = 0
    for caracter in dado_entre_espacos:
        if caracter not in sinais:
            tamanho_palavra += 1
        else:
            pass
    return tamanho_palavra

def tamanho_total_palavras(texto):
    '''Para cada dado entre espaços do texto, a função executará a
    função tamanho_palavra; dessa forma, serão somados os caracteres,
    excluindo os itens da lista sinais da função tamanho_palavra.'''

    dados_entre_espacos = separa_palavras(texto)
    tamanho_total_palavras = 0
    for elemento in dados_entre_espacos:
        tamanho_total_palavras += tamanho_palavra(elemento)
    return tamanho_total_palavras

def remove_sinais(dado_entre_espacos):
    '''A função remove os sinais abaixo de um dado entre espaços 
    (palavras e sinais de pontuação), restando então palavras
    isoladas.
    ,:;.!?'''
    # Minha primeira utilização da biblioteca re.

    dado_entre_espacos = re.split(r'[,:;.!?]+', dado_entre_espacos)
    for elemento in dado_entre_espacos:
        if elemento == '':
            del elemento
        else:
            pass
    return dado_entre_espacos[0]

def tira_sinais_de_dados_entre_espacos(lista_dados_entre_espacos):
    '''A função recebe uma lista em que cada elemento é uma palavra com
     ou sem sinais de pontução: se a palavra estiver isolada, nada 
    acontece; se a palavra estiver ao lado de sinais de pontuacao, ela 
    será isolada desses sinais.
    '''
    percorre_dados = 0
    for dado_entre_espacos in lista_dados_entre_espacos:
        lista_dados_entre_espacos[percorre_dados] =\
        remove_sinais(lista_dados_entre_espacos[percorre_dados])
        percorre_dados += 1
    lista_de_palavras = lista_dados_entre_espacos
    return lista_de_palavras

def palavras_texto(texto):
    palavras = tira_sinais_de_dados_entre_espacos(separa_palavras(texto))
    return palavras

def n_total_caracteres_por_frase(texto):
    lista_sentencas = separa_frases(texto)
    tamanho_total_frases = 0
    for frase in lista_frases:
        tamanho_frase = total_caracteres_sem_espaco(frase)
        tamanho_total_frases += tamanho_frase
    return tamanho_total_frases

# /|\ Assinatura do texto: \|/

# a) tamanho médio de palavra

def assinatura_1_tamanho_medio_palavras(texto):
    '''Para calcular o tamanho médio das palavras, divide-se a soma
    dos tamanhos das palavras pelo tamanho total de palavras.
    '''
    tamanho_medio_palavras =\
        tamanho_total_palavras(texto) / total_palavras(texto)
    return tamanho_medio_palavras

# b) relação type-token

def assinatura_2_relacao_type_token(texto):
    '''Número de palavras diferentes dividido pelo número total de
    palavras.
    '''
    palavras_diferentes = n_palavras_diferentes(palavras_texto(texto)) 
    return palavras_diferentes / total_palavras(texto)

def assinatura_3_razao_hapax_legomana(texto):
    '''Número de palavras diferentes dividido pelo número total de
    palavras.
    '''
    palavras_unicas = n_palavras_unicas(palavras_texto(texto)) 
    return palavras_unicas / total_palavras(texto)

def assinatura_4_tamanho_medio_sentenca(texto):
    '''Soma caracteres de todas as sentenças dividido pelo número de
    sentenças.
    '''
    n_total_sentencas = total_sentencas(texto)
    n_total_caracteres = 0   
    lista_sentencas = separa_sentencas(texto)
    for sentenca in lista_sentencas:
        n_total_caracteres += total_caracteres_com_espacos(sentenca)
    return n_total_caracteres / n_total_sentencas
    
def assinatura_5_complexidade_de_sentenca(texto):
    '''Número total de frases dividido pelo número total de sentenças
    '''
    n_total_de_frases = total_frases(texto)
    n_total_sentencas = total_sentencas(texto)
    return n_total_de_frases / n_total_sentencas

def assinatura_6_tamanho_medio_de_frase(texto):
    '''Número total de caracteres por frase dividido pelo número de 
    frases no texto.
    '''
    n_total_de_frases = total_frases(texto)
    frases = ''
    n_total_caracteres = 0
    lista_sentencas = separa_sentencas(texto)
    for sentenca in lista_sentencas:
        sentenca = separa_frases(sentenca)
        for frase in sentenca:
            n_total_caracteres += len(frase)
    return n_total_caracteres / n_total_de_frases

#======================================================================

# /|\ Comparar assinaturas: \|/

# 2 - Esse deve ser o segundo item;
def compara_assinatura(as_a, as_b): 
    grau_similaridade_as_a_as_b = ( abs(as_a[0] - as_b[0])
                                  + abs(as_a[1] - as_b[1]) 
                                  + abs(as_a[2] - as_b[2]) 
                                  + abs(as_a[3] - as_b[3]) 
                                  + abs(as_a[4] - as_b[4]) 
                                  + abs(as_a[5] - as_b[5]) 
    )                             / 6
    return grau_similaridade_as_a_as_b

# /|\ Avaliar textos: \|/

# 3 - E por fim, o último item.
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma 
    assinatura ass_cp e deve devolver o numero (1 a n) do texto com 
    maior probabilidade de ter sido infectado por COH-PIAH.'''

    '''Para poder informar qual é o texto cujo estilo é o mais 
    semelhante ao do texto do aluno que sabe-se estar infectado com
    COH-PIAH, n_texto registrará a cada iteração do loop for qual o
    texto atual, e, se o g_simil da iteração for menor do que o 
    menor_g_simil, identificador_texto_mais_similar assumirá o valor 
    de n_texto, e esse valor é o que será informado ao usuário.'''
    n_texto = 1
    identificador_texto_mais_similar = 0
    # Menor grau de similaridade - irá registrar o número texto com
    # menor g_simil; inicia em 1 pois os humanos iniciam a contagem do
    # número 1.
    menor_g_simil = 100
    for texto in textos:
        # O grau de similaridade compara a assinatura do texto e
        # compara a assinatura do aluno infectado com COH-PIAH.
        g_simil = compara_assinatura(calcula_assinatura(texto), ass_cp)
        if g_simil < menor_g_simil:
            menor_g_simil = g_simil
            identificador_texto_mais_similar = n_texto
        else:
            pass
        n_texto += 1
    return identificador_texto_mais_similar

def main():
    ass_aluno_infectado = le_assinatura()
    print()
    lista_textos = le_textos()
    n_texto_infectado = avalia_textos(lista_textos, ass_aluno_infectado)
    print('\nO autor do texto', n_texto_infectado,'está infectado com COH-PIAH')
main()