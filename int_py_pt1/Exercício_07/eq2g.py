def main():

    print(bask(int(input("a = ")), int(input("b = ")), int(input("c = "))))

def delta(a, b, c):

    return ((b**2) - (4*a*c))

def bask(a, b, c):
    
    d = delta(a, b, c)
    if d > 0:
        import math
        print('\t{0:_^22}'.format('delta '), '=', d)
        print ('\traiz quadrada de delta =', '{0:.2f}'.format(math.sqrt(d)))    
    elif d == 0:
        print('\tdelta =', d)
    elif d < 0:
        #e = len(str(d)) + 8
        print('\tdelta =', d)
        print('\t(negativo)')
        #print('\t{0:_^13}'.format('(negativo)'))
        #tentar usar o parâmetro 'e' para setar {0:_^13}; não sei como fazer 2021-04-08
    
    if d > 0:
        X1 = ((-b) + (math.sqrt(d)))/(2*a)
        X2 = ((-b) - (math.sqrt(d)))/(2*a)
        print("\nx1 =", '{0:.2f}'.format(X1),"e x2 =", '{0:.2f}'.format(X2))
        #print("\nx1 e x2 =", end=" ")
        return X1, X2   
    elif d == 0:
        print("\nx = ", end=" ")
        return (-b)/(2*a)
    elif d < 0:
        return ("\nEsse número não tem raízes reais.")

main()