import datetime as dt

from fila import Fila
from pessoa import Pessoa


class FilaPreferencial(Fila):
    def __init__(self):
        super().__init__()
        self.preferencial = []
        self.chamada_preferencial = 0
    
    def yr(self):
        return int(dt.date.today().strftime('%Y'))

    def push(self, pessoa):
        if not isinstance(pessoa, Pessoa):
            print('Só podem ser adicionadas instâncias da classe Pessoa a uma instância da classe FilaPreferencial.')
            return
        if pessoa.ano_nasc > self.yr():
            print(f'O ano de nascimento não pode ser maior que {self.yr()}.')
            return
        if self.yr() - pessoa.ano_nasc >= 60:
            self.preferencial.append(pessoa)
            print(f' + {pessoa.nome},  {self.yr()-pessoa.ano_nasc} anos  P({len(self.preferencial)})')
        else:
            self.data.append(pessoa)
            print(f' + {pessoa.nome},  {self.yr()-pessoa.ano_nasc} anos  C({self.size()})')

    def lista_de_chamada(self):
        if len(self.preferencial) > 0:
            print(f'Lista de chamada preferencial ({len(self.preferencial)}):')
            for pessoa in self.preferencial:
                print(f' - {pessoa.nome},  {self.yr()-pessoa.ano_nasc} anos')
        else:
            print('Não há ninguém na lista de chamada preferencial.')
        if self.size() > 0:
            print(f'Lista de chamada comum ({self.size()}):')
            for pessoa in self.data:
                print(f' - {pessoa.nome},  {self.yr()-pessoa.ano_nasc} anos')
        else:
            print('Não há ninguém na lista de chamada comum.')
        if self.size()+len(self.preferencial) > 0:
            print(f'A fila tem {self.size()+len(self.preferencial)} pessoas.')

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
p11=Pessoa('Dalila', 1958)
p12=Pessoa('Anthony', 1949)

fp=FilaPreferencial()

fp.lista_de_chamada()
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
fp.push(p11)
fp.push(p12)

print()
fp.lista_de_chamada()

print("\n * Primeiro, vamos chamar apenas a primeira pessoa, executando a função 'chamar':")
fp.chamar()
print("\n * Vamos então chamar a segunda pessoa, executando a função 'chamar' mais uma vez:")
fp.chamar()
print("\n * Agora vamos chamar o resto da fila de uma vez, executando a função 'chamar_todos':")
fp.chamar_todos()