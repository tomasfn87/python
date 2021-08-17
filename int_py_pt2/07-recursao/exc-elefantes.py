import pytest

def incomodam(n, ready=False, frase=""):
    if ready == False:
        if n < 1:
            return incomodam(n, True)
        else:
            frase = incomodam(0)
            for i in range(0, n):
                frase += ("incomodam ")
            return incomodam(n, True, frase)
    else:
        return frase

def elefantes(n, ready=False, frase=incomodam(0)):
    if ready == False:
        if n < 1:
            return elefantes(n, True)
        else:
            for i in range(1, n + 1):
                if i == 1:
                    frase += "Um elefante incomoda muita gente"
                else:
                    frase += "\n" + str(i) + " elefantes " + incomodam(i) \
                             + "muito mais"
                    if i == n:
                        break
                    else:
                        frase += "\n" + str(i) + " elefantes " + incomodam(1) \
                                 + "muita gente"
            return elefantes(n, True, frase)
    else:
        return frase

@pytest.mark.parametrize("entrada, resultado", [
    (1, "Um elefante incomoda muita gente"),
    (2, "Um elefante incomoda muita gente\
\n2 elefantes incomodam incomodam muito mais"
),
    (3, "Um elefante incomoda muita gente\
\n2 elefantes incomodam incomodam muito mais\
\n2 elefantes incomodam muita gente\
\n3 elefantes incomodam incomodam incomodam muito mais"
),
    (4, "Um elefante incomoda muita gente\
\n2 elefantes incomodam incomodam muito mais\
\n2 elefantes incomodam muita gente\
\n3 elefantes incomodam incomodam incomodam muito mais\
\n3 elefantes incomodam muita gente\
\n4 elefantes incomodam incomodam incomodam incomodam muito mais"
)
])
def test_elefantes(entrada, resultado):
    assert elefantes(entrada) == resultado

# -i interactive version
""" 
def main():
    run = 1
    while run == True:
        n_elefantes = int(input("Insira o número de elefantes: "))
        if n_elefantes == -1:
            break
        elif n_elefantes == 0:
            pass
        else:
            print()
            print(elefantes(n_elefantes))
        print("\nDigite -1 para sair.\n")

main()
"""