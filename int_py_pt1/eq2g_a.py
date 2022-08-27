def main():
	a = float(input("Insira a -> o número multiplicado por x2 (x ao quadrado): "))
	b = float(input("Insira b -> o número multiplicado por x: "))
	c = float(input("Insira c -> o número somado ou subtraído: "))
	d = ((b**2) - (4 * a * c))
			
	if d > 0:
		import math
		raizd = math.sqrt(d)
		xa = (- b + raizd) / (2 * a)
		xb = (- b - raizd) / (2 * a)
		print()
		print("Esta equação possui dois valores reais e distintos:")
		print("  x1 =", xa)
		print("  x2 =", xb)
		
	elif d == 0:
		x = - b / (2 * a)
		print()
		print("Esta equação possui um valor único:")
		print("  x =", x)

	else:
		print()
		print("Esta equação não possui valores reais.")
main()
