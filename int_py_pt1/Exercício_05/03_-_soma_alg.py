def main():

	entrada = int(input("Digite um número inteiro: "))
	numero = entrada
	soma0 = 0

	while numero > 0:
		soma0 = (soma0 + (numero % 10))
		numero = (numero // 10)
	print(soma0)

	Rsoma0 = soma0
	soma1 = 0

main()
