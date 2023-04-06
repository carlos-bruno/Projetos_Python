import os
from random import randint
import sys
import time

clear = lambda: os.system('cls')

def titulo():
    print('*' * 60)
    print(f"{'Adivinhação Númerica':^60}") 
    print('*' * 60)


titulo()

time.sleep(5)

print("Cadastre as informações necessárias !!!")

tentativa = int(input("\nDigite a quantidade de tentativas: "))
inicio = int(input("\nDigite o valor inicial para o range: "))
final = int(input("\nDigite o final para o range: "))

clear()
titulo()
numSecreto = randint(inicio, final)

chute = 0

while numSecreto != chute and tentativa != 0:
    print("Você possui", tentativa,"Tentativas" )
    chute = input("Informe um valor: ")
    if chute.isnumeric():
        chute = int(chute)
        if chute == numSecreto:
            clear()
            titulo()
            print("Parabens você acertou !!!")
            break
        else:
            clear()
            titulo()
            print("Tente novamente \n")
            tentativa -= 1
    else:
        clear()
        titulo()
        print("#ERROR ??? Caractere incorreto. \n\n ****O Programa será finalizado****")
        break
else:
    clear()
    titulo()
    print("Você Perdeu :( o valor informado era", numSecreto,"\nBoa sorte na proxima")