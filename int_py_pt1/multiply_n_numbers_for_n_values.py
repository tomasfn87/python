def main():
	size = int(input("Type sequence size: "))
	print()
	product = 1
	count = 0
	
	while count < size:
		if (count+1) == size:
			print("Type the #", (count+1), "and last value")
		else:
			print("Type the value #", (count+1))
		value = int(input("  to be multiplied: "))
		print()
		product = product*value
		count += 1
	print("The product of this multiplication is:", product)
main()