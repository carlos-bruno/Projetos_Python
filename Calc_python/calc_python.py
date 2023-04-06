from os import system

clear = lambda: system('CLS')

print('CALCULADORA EM PYTHON')

while True:
    operator = input('Informe a operação que você deseja realizar \n'
        '+ para soma\n'
        '- para subtração\n'
        '/ para divisão\n'
        '* para multiplicação\n')
    clear()

    num1 = input('Digite o primeiro valor: ')
    num2 = input('Digite o segundo valor: ')

    clear()

    try:
        num1 = float(num1)
        num2 = float(num2)

    except:
        clear()
        print('Dados não reconhecidos, por favor inicie o programa novamente...')
        break

    if operator == '+':
        soma = num1 + num2
        print(f'A soma entre {num1} e {num2} é {soma}')
        sair = int(input("Digite 1 para sair ou 0 para ficar: "))
        clear()

        if sair == 1:
            break
        else:
            continue

    elif operator == '-':
        subtracao = num1 - num2
        print(f'A subtração entre {num1} e {num2} é {subtracao}')
        sair = int(input("Digite 1 para sair ou 0 para ficar: "))
        clear()
        if sair == 1:
            break
        else:
            continue

    elif operator == '*':
        multiplicacao = num1 * num2
        print(f'A multiplicacao entre {num1} e {num2} é {multiplicacao}')
        sair = int(input("Digite 1 para sair ou 0 para ficar: "))
        clear()

        if sair == 1:
            break
        else:
            continue

    if operator == '/':
        divisao = num1 / num2
        print(f'A divisao entre {num1} e {num2} é {divisao}')
        sair = int(input("Digite 1 para sair ou 0 para ficar: "))
        clear()

        if sair == 1:
            break
        else:
            continue

    else:
        print('Operador invalido !!')
        sair = int(input("Digite 1 para sair ou 0 para ficar: "))
        clear()
        if sair == 1:
            break
        else:
            continue
    


        






