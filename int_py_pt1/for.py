def main():

#	for counter in range(30, 56):
#		print(counter, "Salut")

#	for for_loop_test in range(1, 11, 3):
#		print("Vous êtes numéro", for_loop_test)

#	count = 0
#	for number in range(1, 4):
#		count = count + number
#	print(count)
	
	def sum_list(lista_entrada):
		counter = 0
		for number in lista_entrada:
			counter += 1
			print(counter)
			
		assert sum_list([1, 2, 3]) == 6
		assert sum_list([1, 2, 3, 4]) == 10

main()