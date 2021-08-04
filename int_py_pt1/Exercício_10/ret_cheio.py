def main():

    ent_largura = int(input("digite a largura: "))
    if ent_largura <= 0:
        ent_largura = int(input("largura > 0: "))

    ent_altura = int(input("digite a altura: "))
    if ent_altura <= 0:
        ent_altura = int(input("altura > 0: "))

    altura = ent_altura
    largura = ent_largura

    while altura > 0:
        while largura > 0:
            print('#', end='')
            largura -= 1
        largura = ent_largura
        altura -= 1
        print()
    
    

main()