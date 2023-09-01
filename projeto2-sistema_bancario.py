def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += 'Depósito: R$ {:.2f}\n'.format(valor)
        print('Depósito de R$ {:.2f} realizado com sucesso!'.format(valor))
    else:
        print('Operação falhou! O valor informado é inválido')
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques > limite_saques
        
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
        print('Saque de R${:.2f} realizado com sucesso!'.format(valor))
    else:
        print('Operação falhou! Valor informado é inválido.')
    return saldo, extrato
        


def exibir_extrato(saldo, /, *, extrato):
    print('\n===============EXTRATO================')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print('\nSaldo: R$ {:.2f}'.format(saldo))
    
def criar_usuario(usuarios):
    cpf = input('Informe o CPF:')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('Já existe usuário com esse CPF!')
        return
    nome = input('Informe o nome completo:')
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_cc():
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {'agencia': agencia, "numero_conta": numero_conta, "usuario": usuario}

    print('Usuário não encontrado, fluxo de criação de conta encerrado!')

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
    
def main():

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    
    menu = """
    --MENU--
    [d] = Depositar
    [s] = Sacar
    [e] = Extrato
    [c] = Nova conta
    [u] = Novo usuário
    [l] = Listar contas
    [q] = Sair
    :"""

    while True:
        opcao = input(menu)
        if opcao == 'd':
            valor = float(input('Informe o valor de depósito: R$ '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Informe o valor de saque: R$'))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite,
                                  numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)
            
        elif opcao == 'q':
            print('Sair')
            break
        else:
            print('Operação inválida, por favor selecione novamente a operação desejada.')
        
        
if __name__ == '__main__':
    main()