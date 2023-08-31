menu = """

[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = Sair

"""

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

deposito = []

while True:
    opcao = input(menu)
    if opcao == 'd':
        valor = float(input('Informe o valor de depósito: R$ '))
        if valor > 0:
            saldo += valor
            extrato += 'Depósito: R$ {:.2f}\n'.format(valor)
        else:
            print('Operação falhou! O valor informado é inválido')

    elif opcao == 's':
        valor = float(input('Informe o valor do saque: R$ '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques > LIMITE_SAQUES
        
        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')
        elif excedeu_limite:
            print('Operação falhou! O valor do saque excede o limite.')
        elif excedeu_saque:
            print('Operação falhou! O número de saques foi excedido')
        elif valor > 0:
            saldo -= valor
            extrato += 'Saque: R$ {:.2f}\n'.format(valor)
            numero_saques += 1
        else:
            print('Operação falhou! Valor informado é inválido.')
            
    elif opcao == 'e':
        print('\n===============EXTRATO================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print('\nSaldo: R$ {:.2f}'.format(saldo))
        
    elif opcao == 'q':
        print('Sair')
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')