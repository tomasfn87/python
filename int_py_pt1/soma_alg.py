def main():

	entrada = int(input("Insira um número cujos dígitos você queira que sejam somados: "))
	numero = entrada
	soma0 = 0

	while numero > 0:
		soma0 = (soma0 + (numero % 10))
		numero = (numero // 10)
	print("1) A soma dos algarismos de", entrada,"é igual a", soma0)

	Rsoma0 = soma0
	soma1 = 0

	if Rsoma0 >= 10:
		while Rsoma0 > 0:
			soma1 = (soma1 + (Rsoma0 % 10))
			Rsoma0 = (Rsoma0 // 10)
		print("2) A soma dos algarismos de", soma0,"é igual a", soma1)
		if entrada == 26111987:
			print("S2 Je t'aime beaucoup, mon amour...!")
		else:
			()
	else:
		print("=)")

	Rsoma1 = soma1
	soma2 = 0

	if Rsoma1 >= 10:
		while Rsoma1 > 0:
			soma2 = (soma2 + (Rsoma1 % 10))
			Rsoma1 = (Rsoma1 // 10)
		print("3) A soma dos algarismos de", soma1,"é igual a", soma2)
		if entrada == 22081987:
			print("C'est la vie...")
			print("_\|/_ Cannabis sativa linnæus _\|/_ La médecine _\|/_")
		else:
			()
	elif entrada == 26111987:
		print(";*")
	elif soma0 < 10 and Rsoma1 < 10:
		() #Nada a fazer.
	else:
		print("=)")

main()
