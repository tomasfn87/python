class Construir:

    def __init__(
        self, andares=2, apartamentos=4, palavra1="horizontal", palavra2="vertical"
        ): #       1.              2.          3.                     4.
        '''
        __init__: inicialização da classe Construir;
          definição de: parâmetro="valor-padrão do parâmetro"
    
          Se nenhum valor for passado - Construir() - uma instância de
        Construir assumirá os valores declarados. Portanto:
          meu_predio_01 = Construir(2, 4, "horizontal", "vertical")
        é igual a:
          meu_predio_01 = Construir()
    
        1. Número de andares do prédio
        2. Número de apartamentos por andar
        3. Palavra que será impressa na horizontal
        4. Palavra que será impressa na vertical
        '''
        self.an, self.ap, self.p1, self.p2 = andares, apartamentos, palavra1, palavra2

    def predio(self):
        # Imprime a fachada do nosso edifício (=instância da classe Construir)

        for i in range(0, self.an):
            print(self.ap * (" " + self.p1))
            for char in self.p2:
                print(
                      char
                    + (self.ap * (((len(self.p1)) * " ") + char))
                )
        print(self.ap * (" " + self.p1))
  
    def novoPredio():
        '''Cria uma nova instância da classe Construir na variável 'novo'
        a partir de input do usuário; retorna a variável.'''

        print("Quantos andares tem seu prédio?", end=" ")
        andar = int(input()) # input sempre é str => converte para int
        print("Quantos apartamentos por andar?", end=" ")
        aps = int(input())
        print("Primera palavra que representa o seu lar:", end=" ")
        lar1 = input()
        print("Segunda palavra que representa o seu lar:", end=" ")
        lar2 = input()
        print()
        novo = Construir(andar, aps, lar1, lar2)
        return novo

    def main():

        Cnp, Cp = Construir.novoPredio, Construir.predio
        novo_predio = Cnp()
        Cp(novo_predio)
        print()

Np = Construir.main
Np()