import re
import sys

from limit_empty import limit_empty


def extrair(nome_e_telefone):
    x=re.search('(\D+)\s\(?(\d{2})\)?\s*[-_]?\s*(\d{4,5})\s*[-_]?\s*(\d{4})', nome_e_telefone)
    dados = x.groups()

    nome = dados[0]
    ddd = dados[1]
    telefone_1 = dados[2]
    telefone_2 = dados[3]

    return f'Nome: {limit_empty(nome)},  Tel.: ({ddd}){telefone_1}-{telefone_2}'

if __name__ == '__main__':
    inputs = sys.argv
    if len(inputs) >= 2:
        nome_e_telefone = inputs[1]
        print(extrair(nome_e_telefone))
