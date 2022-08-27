def main():

	print ("Este programa só aceita números inteiros.")
	print ("Insira X e Y do primeiro ponto: ")
	x1 = int(input("X do 1º ponto: "))
	y1 = int(input("Y do 2º ponto: "))
	print ()

	print ("Insira X e Y do segundo ponto: ")
	x2 = int(input("X do 2º ponto: ")) 
	y2 = int(input("Y do 2º ponto: "))
	print ()	

	import math
	dxy = math.sqrt( ((x1 - x2) **2) + ((y1 - y2) **2) )
	
	if dxy >= 10:
		print ("longe")
	else:
		print ("perto")
	
	print ("Distância entre os dois pontos: ", float(dxy))
main()
