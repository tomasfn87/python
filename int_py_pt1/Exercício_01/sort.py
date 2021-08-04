def main():

	print ("Insira 3 números inteiros:")

	n1 = int(input("1º número: "))
	n2 = int(input("2º número: "))
	n3 = int(input("3º número: "))

#1)
#	if n1 <= n2 <= n3:
#		print (n1, n2, n3)
#	elif n1 <= n3 <= n2:
#		print (n1, n2, n3)
#	elif n2<= n1<= n3:
#		print (n2, n1, n3)
#	elif n2<= n3<= n1:
#		print (n2, n3, n1)
#	elif n3<= n1<= n2:
#		print (n3, n1, n2)
#	elif n3<= n2<= n1:
#		print (n3, n2, n1)
#	else:
#		print (n1, n2, n3)

#2)
#	print (sorted([n1, n2, n3]))

#3)
	l1 = [n1, n2, n3]
	l1.sort()
	print (l1)

main()
