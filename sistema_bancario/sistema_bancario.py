def titulo():   
    print('-' * 40)
    print(f"{'Menu':^40}")
    print('-' * 40)
    
    print('[D] - Depositar')
    print('[S] - Sacar')
    print('[E] - Extrato')
    print('[Q] - Sair')
    print('\n')

def depositar():
    
    deposito = float(input('Informe o valor do deposito: '))
    if deposito > 0:
        print('Valor adicionado em sua conta !!!')
        return deposito
    
    else:
        print('Não foi possivel realizar o depósito tente novamente !! ')


def sacar():
    saque = float(input('Informe o valor de saque: '))
    if saque > 0 and saque <= 500 and saque <= saldo:
        print('Saque Realizado com sucesso !!')
        return saque
    
    elif saque > saldo:
        print('Saldo insuficiente para saque')

    else:
        print('Valor acima do limite diario !!')
    

SAQUE_LIMITE = 3
saldo = saques_realizados = 0
extrato = []


while True:
    titulo()

    opcao = input('Escolha uma opção: ').upper()
    
    if opcao == 'D':
        valor_deposito = depositar()
        if valor_deposito is not None: 
            extrato.append(f'Deposito: + R${ valor_deposito:.2f}')
            saldo += valor_deposito
        

    elif opcao == 'S':
        if saques_realizados < SAQUE_LIMITE:
            valor_saque = sacar()   
            if valor_saque is not None:
                extrato.append(f'Saque: - R${ valor_saque:.2f}')
                saques_realizados += 1
                saldo -= valor_saque
        else:
            print('Limite diario de saque realizado !!')

    elif opcao == 'E':
        
        print(f"{' EXTRATO ':=^40}")
        print(*extrato, sep='\n')
        print('Não houve movimentações recentes') if not extrato else None
        print(f'Seu saldo atual: R${ saldo:.2f}')
        print('=' * 40)

    elif opcao == "Q":
        print( "Programa finalizado...")
        break
    
    else:
        print('Opção invalida tente novamente.')



