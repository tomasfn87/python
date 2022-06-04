import datetime as dt

from fila import Fila
from pessoa import Pessoa


class FilaPreferencial(Fila):
    def __init__(self):
        super().__init__()
        self.preferencial = []
        self.chamada_preferencial = 0

    def push(self, pessoa):
        if not isinstance(pessoa, Pessoa):
            print('Só podem ser adicionadas instâncias da classe Pessoa  a uma instância da classe FilaPreferencial.')
            return
        yr = int(dt.date.today().strftime('%Y'))
        if pessoa.ano_nasc > yr:
            print(f'O ano de nascimento não pode ser maior que {yr}.')
            return
        if yr - pessoa.ano_nasc >= 60:
            self.preferencial.append(pessoa)
        else:
            self.data.append(pessoa)

    def chamar(self):
        if len(self.preferencial) == 0 and len(self.data) == 0:
            print('Não tem ninguém na fila.')
            return
        if self.chamada_preferencial == 2 or len(self.preferencial) == 0 and len(self.data) > 0:
            print(f'Chamando {self.top().nome}')
            self.pop()
            if self.chamada_preferencial == 2:
                self.chamada_preferencial = 0
            return
        if self.chamada_preferencial < 2 and len(self.preferencial) > 0:
            print(f'Chamando {self.preferencial[0].nome} (preferencial)')
            self.preferencial.pop(0)
            self.chamada_preferencial += 1
    
    def chamar_todos(self):
        while len(self.preferencial) > 0 or not self.empty():
            self.chamar()
        self.chamar()

p1=Pessoa('Mary', 1950)
p2=Pessoa('Charles', 1980)
p3=Pessoa('Donnald', 1952)
p4=Pessoa('Margareth', 1972)
p5=Pessoa('Charlotte', 1950)
p6=Pessoa('Rebecca', 1958)
p7=Pessoa('Peter', 1992)
p8=Pessoa('Helen', 1997)
p9=Pessoa('Hassan', 1944)
p10=Pessoa('Marcus', 1988)

fp=FilaPreferencial()
print(' * Vamos olhar o conteúdo da fila comum:')
print(f'{fp.data}\n * Pessoas na fila comum: {fp.size()}')

print('\n * Vamos olhar o conteúdo da fila preferencial:')
print(f'{fp.preferencial}\n * Pessoas na fila preferencial: {len(fp.preferencial)}')
print("\n * Vamos executar a função 'chamar' para ver seu comportamento quando a fila está vazia:")
fp.chamar()

fp.push(p1)
fp.push(p2)
fp.push(p3)
fp.push(p4)
fp.push(p5)
fp.push(p6)
fp.push(p7)
fp.push(p8)
fp.push(p9)
fp.push(p10)

print(f'\n * Pessoas adicionadas à fila: {(fp.size() + len(fp.preferencial))}')
print(f" * Como o ano atual é {dt.date.today().strftime('%Y')},")
print(f' * {len(fp.preferencial)} pessoas se enquadrarão na fila preferencial')
print(f' * e {fp.size()} pessoas se enquadrarão na fila comum.')

print('\n * Vamos olhar o conteúdo da fila comum:')
print(f'{fp.data}\n * Pessoas na fila comum: {fp.size()}')

print('\n * Vamos olhar o conteúdo da fila preferencial:')
print(f'{fp.preferencial}\n * Pessoas na fila preferencial: {len(fp.preferencial)}')

print("\n * Primeiro, vamos chamar apenas a primeira pessoa, executando a função 'chamar':")
fp.chamar()
print("\n * Vamos então chamar a segunda pessoa, executando a função 'chamar' mais uma vez:")
fp.chamar()
print("\n * Agora vamos chamar o resto da fila de uma vez, executando a função 'chamar_todos':")
fp.chamar_todos()

print('\n * Muito bom, nosso programa funciona muito bem:')
print(' * observe como ele chama 2 pessoas da fila preferencial para cada pessoa da fila comum,')
print(' * a menos que a fila preferencial esteja vazia.')
