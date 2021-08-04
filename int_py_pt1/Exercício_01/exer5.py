def main():

	print ("Insira 3 números inteiros:")

	n1 = int(input("1º número: "))
	n2 = int(input("2º número: "))
	n3 = int(input("3º número: "))

	if n1 < n2 < n3:
		print ("crescente")
	else:
		print ("não está em ordem crescente")

main()
