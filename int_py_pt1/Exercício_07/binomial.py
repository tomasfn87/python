def fator(x):
    f = 1
    while x >= 2:
        f = f * x
        x -= 1
    return f

def testa_fator():
    if fator(1) == 1:
        print("It works for 1.")
    else:
        print("It doesn't work for 1.")
    if fator(2) == 2:
        print("It works for 2.")
    else:
        print("It doesn't work for 2.")
    if fator(0) == 1:
        print("It works for 0.")
    else:
        print("It doesn't work for 0.")
    if fator(5) == 120:
        print("It works for 5.")
    else:
        print("It doesn't work for 5.")

def binomial(x, y):
    while x <= 0 or y < 0 or x < y:
        x = int(input("Please respect these rules:\nx > 0; y >= 0 and x >= y;\nPlease retype x = "))
        y = int(input("and y = "))
    return (fator(x)) / ((fator(y)) * (fator(x - y)))

print(binomial(int(input("x = ")), int(input("y = "))), '\n')
print(fator(0))
print(fator(1))
print(fator(2))
print(fator(3))
print(fator(4))
print(fator(5))
print(fator(6))
print(fator(7))
print(fator(8))
print(fator(9))
print(fator(10))
print(fator(10*2))
print(fator(10*3))
print(fator(10*4))
print(fator(10*5))
