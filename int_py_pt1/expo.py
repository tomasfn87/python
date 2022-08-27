def main():
	a = int(input("Insira um número: "))
	b = int(input("Insira um número para elevar o primeiro número(k > 0): "))
	if b < 0: 
		b = int(input("O número deve ser >= 0: "))
	
	if b == 0:
		print("todo número elevado a 0 é igual a 1")
	elif b == 1:
		print("todo número elevado a 1 é igual a ele mesmo =", a)
	else: 
		exp = a ** b
		print(a, "elevado a", b,"é igual a", exp)
main()