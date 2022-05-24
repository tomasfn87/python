class Funcionario:
    def __init__(self, nome, data_admissao_ymd, salario):
        self.nome = nome
        self.data_admissao_ymd = data_admissao_ymd
        self.salario = salario
        
    def __repr__(self):
        return f'Nome: {self.nome}\nData de admissão: {Funcionario.formatar_data_admissao_dmy(self)}\nSalário: {Funcionario.formatar_valor_monetario(self, self.salario)}'

    def aumento_salario(self, aumento):
        aumento_de_salario = self.salario * (aumento/100)
        aumento_de_salario = Funcionario.formatar_valor_monetario(self, aumento_de_salario)
        self.salario *= (1 + (aumento / 100))
        salario_aumentado = Funcionario.formatar_valor_monetario(self, self.salario)
        print(f'Aumento de salário para {self.nome}: {aumento_de_salario} ({aumento}%)')
        print(f'Novo salário: {salario_aumentado}')

    def formatar_data_admissao_dmy(self):
        dia = self.data_admissao_ymd[6:8]
        mes = self.data_admissao_ymd[4:6]
        ano = self.data_admissao_ymd[0:4]
        return f'{dia}/{mes}/{ano}'

    def formatar_valor_monetario(self, valor):
        valor = '{:.2f}'.format(valor)
        valor = valor.split('.')
        reais = valor[0]
        centavos = valor[1]
        valor_formatado = f'R${Funcionario.marcar_numero(self, reais)},{centavos}'
        return valor_formatado

    def marcar_numero(self, numero, marcador='.'):
        numero_marcado = ''
        if type(numero) != str:
            numero = str(numero)
        contador = 0
        for i in range(len(numero)-1, -1, -1):
            contador += 1
            numero_marcado = numero[i] + numero_marcado
            if contador % 3 == 0 and i != 0:
                numero_marcado = marcador + numero_marcado
        return numero_marcado

class Gerente(Funcionario):
    def __init__(self, nome, data_admissao_ymd, salario, bonus):
        super().__init__(nome, data_admissao_ymd, salario)
        self.bonus = bonus

    def calcular_bonus(self):
        return self.salario * (self.bonus / 100)

    def ver_bonus(self):
        bonus = Funcionario.formatar_valor_monetario(self, Gerente.calcular_bonus(self))
        return f'Bônus sobre o salário de {self.nome}: {bonus} ({self.bonus}%)'

    def ver_salario_com_bonus(self):
        salario_com_bonus = Funcionario.formatar_valor_monetario(self, (self.salario + Gerente.calcular_bonus(self)))
        return f'Salário com bônus: {salario_com_bonus}'

funcionario1 = Funcionario('Tomás', '20220517', 1500)
print(funcionario1)
print()

funcionario1.aumento_salario(5)
print()
print(funcionario1)
print()

gerente1 = Gerente('Kleber', '20120422', 3000, 10)
print(gerente1)
print()
print(gerente1.ver_bonus())
print(gerente1.ver_salario_com_bonus())
