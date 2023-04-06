from random import randint

def computador(escolhas_maquina):
    escolha_maquina = escolhas_maquina[randint(0,2)]
    return escolha_maquina

def comparacao(player, machine):
    if player == machine:
        print("Empate")

    elif player == 'Pedra' and machine == 'Tesoura':
        print('Jogador venceu!!!')

    elif player == 'Tesoura' and machine == 'Papel':
        print('Jogador venceu!!!')

    elif player == 'Papel' and machine == 'Pedra':
        print('Jogador venceu!!!')

    else:
        print('Computador venceu!!!')

while True:
    lista = ['Pedra', 'Papel', 'Tesoura']
    jogador = input('Digite Pedra Papel ou Tesoura: ')

    if jogador.isalpha() and jogador in lista:
        maquina = computador(lista)
        
        print(f'O jogador escolheu {jogador}')
        print(f'A maquina escolheu {maquina}')

        comparacao(jogador, maquina)
        
        tecla = input('Digite qualquer tecla para continuar ou 0 para sair: ')

        if tecla == '0':
            print('O programa será finalizado...')
            break
    else:
        print('Dados informados invalidos, por favor tente novamente!!!')




  



