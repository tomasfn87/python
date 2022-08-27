def main():

    print('\n1)')
    print("""   uma string
multilinhas
    pra escrever
poesias
    clássicas
e concretinhas"""'\n')

    print('\n2)')
    print(r"usando o parâmetro r (Raw String) antes do primeiro quote_mark e as ferramentas '\' e '\n' - fim de r\"\"", "\nagora:\npulou linha?\nsim.\nimprimiu \\n?\nsim.")

    print('\n3)')
    carro = 'uma Ferrari'
    cavalo = 550
    print("Um carro desses bixo, {0}... baita máquina! {1} cavalos de potência!".format(carro, cavalo))
    print("Um carro desses bixo, {}... baita máquina! {} cavalos de potência!".format(carro, cavalo))

    print('\n4)')
    print(r'testando o comando \ no fim da linha (continuar a string na linha abaixo sem imprimir em uma outra linha):')
    print("vamos lá, quero esse texto em uma\
 única linha. A \\ equivale a um toque na barra de espaço em 'print'")

    print('\n5)')
    print("testando \\t: o que faz \\t?")
    print("\tdá um espaço equivalente a apertar 'tab' no teclado.\n\té isso")

main()