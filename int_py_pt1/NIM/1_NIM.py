def computador_escolhe_jogada(n, m):
    if n == 1:
        n = n - 1
        print('\nO computador tirou uma peça.\nFim do jogo! O computador ganhou!')
    elif n == m:
        n = n - m
        if n == 1:
            print('\nO computador tirou uma peça.\nFim do jogo! O computador ganhou!')
        else:
            print('\nO computador tirou', m,'peças.\nFim do jogo! O computador ganhou!')
    elif m == 1:
        n = n - m
        if n == 1:
            print('\nO computador tirou uma peça.\nAgora resta uma peça no tabuleiro.')
            usuario_escolhe_jogada(n, m)
        else:
            print('\nO computador tirou uma peça.\nAgora restam', n,'peças no tabuleiro.')
            usuario_escolhe_jogada(n, m)      
    elif (n - m) % (m + 1) == 0:
        n = n - m
        print('\nO computador tirou', m,'peças.\nAgora restam', n,'peças no tabuleiro.')
        usuario_escolhe_jogada(n, m)
        '''elif m > 1 and (n - m - 1) % (m + 1) == 0:
        n = n - m - 1
        print('\nO computador tirou', (m - 1),'peças.')
        usuario_escolhe_jogada(n, m)'''
    elif n < m:
        N = n
        n = n - N
        if n == 1:
            print('\nO computador tirou uma peça.')
        else:
            print('\nO computador tirou', N,'peças.')
        print('Fim  do jogo! O computador ganhou!')
    else:
        m1 = m
        n = n - m1
        print('\nO computador tirou', m1,'peças.\nAgora restam', n,'peças no tabuleiro.')
        usuario_escolhe_jogada(n, m)


def usuario_escolhe_jogada(n, m):
    print()
    M = int(input('Quantas peças? '))#M é a entrada do usuário para subtrair de n, M <= m
    while M > m:
        M = int(input('Oops! Jogada inválida! Tente de novo. '))
    n = n - M
    if M == 1:
        print('\nVocê tirou uma peça.')
    else:
        print('\nVocê tirou', M,'peças.')
    if n == 1:
        print('Resta apenas uma peça no tabuleiro.')
    else:   
        print('Agora restam', n,'peças no tabuleiro.')
    computador_escolhe_jogada(n, m)

def partida():
    n = int(input("Insira o valor de n (total de peças): "))
    if n < 2:
        n = int(input("n >= 2, insira novamente o valor de n: "))
    m = int(input("Insira o valor de m, m < n (máximo de peças por jogada): "))
    if m >= n:
        m = int(input(" Obedeça m < n! Insira novamente o valor de m: "))

    if n % (m + 1) == 0:
        print('\nVocê começa!')
        usuario_escolhe_jogada(n, m)
    else:
        print('\nComputador começa!')
        computador_escolhe_jogada(n, m)

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

main()