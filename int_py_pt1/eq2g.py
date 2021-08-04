def main():
	a = int(input("Insira a -> o número multiplicado por x2 (x ao quadrado): "))
	b = int(input("Insira b -> o número multiplicado por x: "))
	c = int(input("Insira c -> o número somado ou subtraído: "))
	d = ((b**2) - (4 * a * c))
			
	if d > 0:
		import math
		raizd = math.sqrt(d)
		xa = (- b + raizd) / (2 * a)
		xb = (- b - raizd) / (2 * a)
		if xa < xb:
			print ("as raízes da equação são", xa,"e", xb)
		else:
			print ("as raízes da equação são", xb,"e", xa)

		
	elif d == 0:
		x = - b / (2 * a)
		print("a raiz dupla desta equação é", x)

	else:
		print("esta equação não possui raízes reais")
main()
