def main():
	num = int(input("Insira o primeiro número inteiro para começarmos a contagem: "))

	p = 0
	i = 0

	if num % 2 == 0:
		p = p + 1
		print ("Temos 1 número par")
		print ()
		print ("Pressione CTRL + Z para sair do programa.")
		print ()
	else:
		i = i + 1
		print ("Temos 1 número ímpar")
		print ()
		print ("CTRL + Z = sair do programa")
		print ()

	while p != 0 or i != 0 :
		num = int(input("Insira mais um número inteiro: "))
		if num % 2 == 0:
			p = p + 1
		else: 
			i = i + 1

		if p == 1 and i == 1:
			print ("Temos 1 número par e 1 número ímpar")
			print ()
			print ("CTRL + Z = sair do programa")
			print ()
		elif p > 1 and i == 0:
			print ("Temos", p, "números pares")
			print ()
			print ("CTRL + Z = sair do programa")
			print ()
		elif p == 0 and i > 1:
			print ("Temos", i, "números ímpares")
			print ()
			print ("CTRL + Z = sair do programa")
			print ()
		elif p == 1 and i > 1:
			print ("Temos 1 número par e", i, "números ímpares")
			print ()
			print ("CTRL + Z = sair do programa")
			print ()
		elif p > 1 and i == 1:
			print ("São", p, "números pares e 1 número ímpar")
			print ()
			print ("CTRL + Z = sair do programa")
			print ()
		else:
			print ("São", p, "números pares e", i, "números ímpares")
			print ()
			print ("CTRL + Z = sair do programa")
			print ()
#------------------------------

main()
