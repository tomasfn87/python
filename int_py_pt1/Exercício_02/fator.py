def main():

	entrada = int(input("x! = ? Insert x: "))
	fat = 1
	count = 2
	
	while count <= entrada:
		fat = fat*count
		count += 1
	print(fat)
	
main()