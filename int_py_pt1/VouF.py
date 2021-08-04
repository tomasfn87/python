def main():
	iis_ready = int(input("Digite 1 para Verdadeiro et 0 para Falso: "))

	if iis_ready == 1:
		is_ready = True
		print("Verdade...")
	elif iis_ready == 0:
		is_ready = False
		print("Falso!")
	else:
		print("Digite 1 ou 0, por favor.")

main()
