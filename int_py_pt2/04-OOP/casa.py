class Construir:

    def __init__(self, andares, apartamentos, palavra):
        #                int        int         str
        self.And, self.Apa, self.Pal = andares, apartamentos, palavra

    def casa(self):
    	for i in range(0, self.And):
    	    print(self.Apa * ("  " + self.Pal))
    	    for char in self.Pal:
    		    print(char + (self.Apa * (((len(self.Pal) + 1) * " ") + char)))
    	print(self.Apa * ("  " + self.Pal))

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
        #Casa()
        #Casa("house")
        Construir.novaCasa()
        print()

nc = Construir.main
nc()