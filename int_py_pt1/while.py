num = 20

while num > 0:
	if num % 2 == 0:
		print(num)
	else:
		if num == 1:
			print("I played DooM only once!")
		else:
			print("I played DooM", num, "times.")
	num -= 1