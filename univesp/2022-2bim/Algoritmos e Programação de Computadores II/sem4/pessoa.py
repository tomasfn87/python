import datetime as dt

class Pessoa:
    def __init__(self, nome, ano_nasc):
        self.nome = nome
        self.ano_nasc = int(ano_nasc)

    def __repr__(self):
        yr = int(dt.date.today().strftime('%Y'))
        return f'{self.nome}; {yr - self.ano_nasc} anos'