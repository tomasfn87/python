ent_largura = int(input("digite a largura: "))
if ent_largura <= 0:
    ent_largura = int(input("largura > 0: "))

ent_altura = int(input("digite a altura: "))
if ent_altura <= 0:
    ent_altura = int(input("altura > 0: "))

altura = ent_altura
largura = ent_largura

while altura > 0:
    if altura == ent_altura or altura == 1:
        while largura > 0:
            print('#', end='')
            largura -= 1
        largura = ent_largura
        altura -= 1
        print() 
    else:
        while largura > 0:
            if largura == ent_largura:
                print('#', end='')
                largura -= 1
            elif largura < ent_largura and largura > 1:
                while largura > 1:
                    print(' ', end='')
                    largura -= 1
            elif largura == 1:
                print('#', end='')
                largura -= 1
        largura = ent_largura
        altura -= 1
        print()
