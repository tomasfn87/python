#Create a list through input()
def main():
	entrada_string = input('Insira números de uma lista separados por 1 toque na barra de espaço: ')
	lista = entrada_string.split()
	#imprimir_lista
	print("Ordem numérica: ", sorted(lista, key=int))
	
	for Lista in range(len(lista)):
		lista[Lista] = int(lista[Lista])
		
	print("Soma = ", sum(lista))
main()