class Bhaskara:
    def delta(a, b, c):
        return ((b**2) - (4*a*c))

    def calcular_raizes(a, b, c):
        d = Bhaskara.delta(a, b, c)
        if d > 0:
            import math
            X1 = ((-b) + (math.sqrt(d)))/(2*a)
            X2 = ((-b) - (math.sqrt(d)))/(2*a)
            return 2, X1, X2
        elif d == 0:
            X = (-b)/(2*a)
            return 1, X
        elif d < 0:
            return 0

    def main():
        a = int(input("Digite o valor de a = "))
        b = int(input("Digite o valor de b = "))
        c = int(input("Digite o valor de c = "))
        print(Bhaskara.calcular_raizes(a, b, c))