def main():

	n = int(input("Insira o número a ser verificado: "))

	if (n % 3 == 0) and (n % 5 == 0):
		print ("FizzBuzz")
	else:
		print (n)

main()
