saldo = 0.0
extrato = []  # Lista para armazenar as operações


def adicionarDinheiro(valor):
    """Função para adicionar dinheiro (depósito)"""
    global saldo, extrato
    
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        return True
    return False


def sacarDinheiro(valor):
    """Função para sacar dinheiro"""
    global saldo, extrato
    
    if valor > 0 and valor <= saldo:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        return True
    return False


def mostrarExtrato():
    """Função para mostrar o extrato"""
    print()
    print("===== EXTRATO =====")
    
    if len(extrato) == 0:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in extrato:
            print(operacao)
    
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=" * 20)


opcao = None
while(opcao != '4'):
    print()
    print('========================================')
    print('               MENU')
    print('========================================')
    print('1 - Adicionar Dinheiro')
    print('2 - Sacar Dinheiro')
    print('3 - Mostrar Extrato')
    print('4 - Sair')
    print('========================================')
    
    if(opcao == '1'): 
        print()
        print('ADICIONAR DINHEIRO =====================')
        valor = float(input('Valor do depósito: R$ '))
        
        if adicionarDinheiro(valor):
            print()
            print('Depósito realizado com sucesso!')
            print(f'Saldo atual: R$ {saldo:.2f}')
        else:
            print()
            print('Erro: O valor do depósito deve ser positivo!')
    
    elif(opcao == '2'): 
        print()
        print('SACAR DINHEIRO =========================')
        valor = float(input('Valor do saque: R$ '))
        
        if sacarDinheiro(valor):
            print()
            print('Saque realizado com sucesso!')
            print(f'Saldo atual: R$ {saldo:.2f}')
        else:
            print()
            if valor <= 0:
                print('Erro: O valor do saque deve ser positivo!')
            else:
                print('Saldo insuficiente para realizar o saque.')
                print(f'Saldo disponível: R$ {saldo:.2f}')
    
    elif(opcao == '3'): 
        mostrarExtrato()
    
    elif(opcao == '4'): 
        print()
        print('Obrigado por usar nosso sistema bancário!')
        print('Encerrando o programa...')
        break
    
    elif(opcao != None): 
        print()
        print('Opção não existe! Digite um número de 1 a 4.')
    
    print()
    opcao = input('Opção desejada: ')