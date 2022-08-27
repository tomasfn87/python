def computador_escolhe_jogada(n, m):
    if m == 1:
        subC = 1
    elif n <= m:
        subC = n
    elif n == m + 1:
        subC = m
    elif n > m + 1 and n % (m + 1) != 0:#o NÃO é o !=
        subC =  n % (m + 1)      
    else:
        subC = m
    return subC
    '''Aqui temos o caso quando n é maior que m + 1 e n NÃO é multiplo de (m + 1) - essa 
    é a chave do problema, pois é quando vamos subtrair o RESTO (%) da operação [n % 
    (m + 1)] para deixar o valor restante n como múltiplo de (m + 1), a fórmula para que
    computador sempre vença. É a mesma lógica do início da partida (quem começa), mas 
    aplicada de forma diferente (para determinar qual valor subC  deve ser subtraido de n
    para que a condição {   n % m + 1 == 0}).'''
def usuario_escolhe_jogada(n, m):
    subU = int(input('\nQuantas peças você vai tirar? '))
    if subU > m or subU <= 0:
        subU = int(input('Oops! Jogada inválida! Tente de novo. '))
    return subU

def partida():
    Computador = 0
    Jogador = 0

    n = int(input("Insira o valor de n (total de peças): "))
    if n < 1:
        n = int(input("n >= 1, insira novamente o valor de n: "))

    m = int(input("Insira o valor de m (máximo de peças por jogada): "))
    if m <= 0:
        m = int(input(" Obedeça m < n e m > 0. Insira novamente o valor de m: "))

    if n % (m + 1) == 0:
        print('\nVocê começa!')
        while Computador == 0 or Jogador == 0: 
            subU = usuario_escolhe_jogada(n, m)
            n = n - subU
            if subU == 1:
                print('\nVocê tirou uma peça.')
            else:
                print('\nVocê tirou', subU,'peças.')
            if n <= 0:
                Jogador += 1
                print('Fim do jogo! O jogador ganhou!')
                break
            elif n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            elif n > 1:
                print('Agora restam', n,'peças no tabuleiro.')
            subC = computador_escolhe_jogada(n, m)
            n = n - subC
            if subC == 1:
                print('\nO computador tirou uma peça.')
            else:
                print('\nO computador tirou', subC,'peças.')
            if n <= 0:
                Computador += 1
                print('Fim do jogo! O computador ganhou!')
                break
            elif n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            elif n > 1:
                print('Agora restam', n,'peças no tabuleiro.')          
    else:
        print('\nComputador começa!')
        while Computador == 0 or Jogador == 0:
        #while not n <= 0:
            subC = computador_escolhe_jogada(n, m)
            n = n - subC
            if subC == 1:
                print('\nO computador tirou uma peça.')
            else:
                print('\nO computador tirou', subC,'peças.')
            if n <= 0:
                break
            elif n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            elif n > 1:
                print('Agora restam', n,'peças no tabuleiro.') 
            subU = usuario_escolhe_jogada(n, m)
            n = n - subU
            if subU == 1:
                print('\nVocê tirou uma peça.')
            else:
                print('\nVocê tirou', subU,'peças.')
            if n <= 0:
                Computador += 1
                break
            elif n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            elif n > 1:
                print('Agora restam', n,'peças no tabuleiro.')
        print('Fim do jogo! O computador ganhou!')

def campeonato():
    contPartidas = 1
    placarJogador = 0
    placarComputador = 0
    while contPartidas <= 3:
        print('\n**** Rodada', contPartidas,'****')
        partida()
        contPartidas += 1
        placarComputador += 1
    print('\n**** Final do campeonato ****')
    print('\nPlacar: Você',placarJogador,'X',placarComputador,'Computador')

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada ")
    inicio = input("2 - para jogar um campeonato ")
    while inicio != str(1) and inicio != str(2): #aceita apenas 1 ou 2
        inicio = input("Digite 1 ou 2 e aperte ENTER: ")
    if inicio == str(1):
        print ("\nVocê escolheu uma partida!")
        partida()
    elif inicio == str(2):
        print ("\nVocê escolheu um campeonato!")
        campeonato()
    
    print('\n**** ****\n\nPressione:\n\t"CTRL+ C" se estiver no Windows ou no Linux')
    print('\nou\n\t"Cmnd + Q" no macOS\npara interromper.')

    print("\nVamos jogar mais um NIM? Escolha:\n")
    print("1 - para jogar uma partida isolada ")
    inicio = input("2 - para jogar um campeonato ")
    while inicio != str(1) and inicio != str(2): #aceita apenas 1 ou 2
        inicio = input("Digite 1 ou 2 e aperte ENTER: ")
    if inicio == str(1):
        print ("\nVocê escolheu uma partida!")
        partida()
    elif inicio == str(2):
        print ("\nVocê escolheu um campeonato!")
        campeonato()

main()
