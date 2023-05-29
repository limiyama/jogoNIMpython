#Você conhece o jogo do NIM? Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam  alternadamente, retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.
#Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.
#**** Rodada 1 ****
def computador_escolhe_jogada(a, b):
    jogadaPC = 1
    while jogadaPC != b:
        if (a - jogadaPC) % (b+1) == 0:
            return jogadaPC
        else:
            jogadaPC += 1
    return jogadaPC

def usuario_escolhe_jogada(a, b):
    jogadaValida = False

    while not jogadaValida:
        jogada = int(input('Quantas peças você vai tirar? '))
        if jogada > b or jogada < 1:
            print('\nOops! Jogada inválida! Tente de novo.\n')
        else:
            jogadaValida = True
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if (n % (m+1) == 0):
        print("\nVoce começa!\n")
        vezComputador = False
    else:
        print("\nComputador começa!")
        vezComputador = True

    while n > 0:
        if vezComputador:
            pecaComputador = computador_escolhe_jogada(n, m)
            n = n - pecaComputador
            if pecaComputador == 1:
                print("\nO computador tirou uma peça.")
            else:
                print("\nO computador tirou", pecaComputador, "peças")
            vezComputador = False
        else:
            pecaJogador = usuario_escolhe_jogada(n, m)
            n = n - pecaJogador
            if pecaJogador == 1:
                print("\nVocê tirou uma peça")
            else:
                print("Você tirou", pecaJogador, "peças")
            vezComputador = True
        if (n == 1):
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            if(n != 0):
                print("Agora restam",n,"peças no tabuleiro.\n")
    print("Fim do jogo! O computador ganhou!")

def campeonato():
    n_rodadas = 1
    while n_rodadas <= 3:
        print(f"\n**** Rodada {n_rodadas} ****\n")
        partida()
        n_rodadas += 1
    print("\n**** Final do campeonato! ****\nPlacar: Você 0 X 3 Computador")

def inicio():
    escolha = int(input("Bem-vindo ao jogo do NIM! Escolha:\n \n1 - para jogar uma partida isolada\n2 - para jogar um campeonato"))
    if (escolha == 1):
        print("\nVoce escolheu uma partida isolada")
        partida()
    else:
        print("\nVoce escolheu um campeonato!")
        campeonato()

inicio()