def main():

	iNum = int(input("Insira o número a ser contado (n > 0): "))
	vNum = iNum
	iAlg = int(input("Insira o algarismo a ser contado (0 a 9): "))
	aCon = 0
	
	
	while vNum > 0:
		if vNum % 10 == iAlg:
			aCon += 1
		vNum = int(vNum // 10)
		
	if aCon == 0:
		print (iAlg, "não aparece em", iNum)
	elif aCon == 1: 
		print (iAlg, "aparece apenas uma vez em", iNum)
	else:
		print (iAlg, "aparece", aCon,"vezes em", iNum)
main()