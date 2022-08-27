import math

a = float(input("X do 1º ponto: "))
b = float(input("Y do 1º ponto: "))

c = float(input("X do 2º ponto: ")) 
d = float(input("Y do 2º ponto: "))

sub_ac = (a - c)
sub_bd = (b - d)
di = math.sqrt((sub_ac**2) + (sub_bd**2))

if di >= 10:
	print ("longe")
else:
	print ("perto")
