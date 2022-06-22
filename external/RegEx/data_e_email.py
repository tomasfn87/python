import re
import sys

def extrair(data_e_email):
    regex = '\s*(\d{4}-\d{1,2}-\d{1,2})\s+([a-z]\w+@[a-z]\w+.\w+)\s*'
    x=re.search(regex, data_e_email, flags=re.I)
    dados=x.groups()
    data = dados[0].split('-')
    ano = data[0]
    mes = data[1].rjust(2, '0')
    dia = data[2].rjust(2, '0')
    email = dados[1]
    return f'Data: {ano}/{mes}/{dia},  e-mail: {email}'

if __name__ == '__main__':
    inputs = sys.argv
    if len(inputs) >= 2:
        data_e_email = inputs[1]
        print(extrair(data_e_email))