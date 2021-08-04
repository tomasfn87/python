def main():

	soma = 0
	entrada = int(input("Insira o primeiro número a ser somado: "))

	soma = soma + entrada
	print("O primeiro número é ", soma)
	print()
	while entrada != 0:
		entrada = int(input("Insira o próximo número a ser somado: "))
		print()
		soma = soma + entrada
		print("(Pressione CTRL + Z para interromper o  programa.)")
		print()
		print("A soma é", soma)

main()