class Funcionario:
    def __init__(self, nome, data_admissao_ymd, salario):
        self.nome = nome
        self.data_admissao_ymd = data_admissao_ymd
        self.salario = salario

    def aumento_salario(self, aumento):
        self.salario *= (1 + (aumento / 100))

    def formatar_data_admissao_dmy(self):
        dia = self.data_admissao_ymd[6:8]
        mes = self.data_admissao_ymd[4:6]
        ano = self.data_admissao_ymd[0:4]
        return f'{dia}/{mes}/{ano}'

    def formatar_valor_monetario(self, valor):
        valor_formatado = 'R${:.2f}'.format(valor)
        return valor_formatado.replace('.', ',')

    def __repr__(self):
        return f'Nome: {self.nome}\nData de admissão: {Funcionario.formatar_data_admissao_dmy(self)}\nSalário: {Funcionario.formatar_valor_monetario(self, self.salario)}'

class Gerente(Funcionario):
    def __init__(self, nome, data_admissao_ymd, salario, bonus):
        super().__init__(nome, data_admissao_ymd, salario)
        self.bonus = bonus
        
    def calcular_bonus(self):
        return self.salario * (self.bonus / 100)
    
    def ver_bonus(self):
        bonus = Funcionario.formatar_valor_monetario(self, Gerente.calcular_bonus(self))
        return f'Bônus: {bonus}'

    def ver_salario_com_bonus(self):
        salario_com_bonus = Funcionario.formatar_valor_monetario(self, (self.salario + Gerente.calcular_bonus(self)))
        return f'Salário com bônus: {salario_com_bonus}'

funcionario1 = Funcionario('Tomás', '20220517', 1500)
print(funcionario1)
print()

funcionario1.aumento_salario(5)
print(funcionario1)
print()

gerente1 = Gerente('Kleber', '20120422', 3000, 10)
print(gerente1)
print(gerente1.ver_bonus())
print(gerente1.ver_salario_com_bonus())