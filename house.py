class Construir:
    
    def __init__(self, andares, apartamentos, palavra):
        
        self.an = andares
        self.ap = apartamentos
        self.pa = palavra

    def casa(self):

    	for i in range(0, self.an):
    	    print(self.ap * ("  " + self.pa))
    	    for char in self.pa:
    		    print(
                    char
                  + (self.ap * (((len(self.pa) + 1) * " ") + char))
                )
    	print(self.ap * ("  " + self.pa) + " ")

    def novaCasa():

        print("Quantos andares tem seu prédio?", end=" ")
        andar = int(input())
        print("Quantos apartamentos por andar?", end=" ")
        aps = int(input())
        print("Uma palavra que representa o seu lar:", end=" ")
        lar = input()
        print()
        nova = Construir(andar, aps, lar)
        Construir.casa(nova)

    def main():
        
        Construir.novaCasa()
        print()

nc = Construir.main
nc()