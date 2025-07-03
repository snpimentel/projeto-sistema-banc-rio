menu = '''
====== DEGITE O NÚMERO DA OPÇÃO DESEJADA ======
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=>'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Cria um loop infinito até que o usuário deseje sair
while True:
    # Exibe o menu e armazena a opção escolhida pelo usuário
    opcao = input(menu)

    # Verifica se a opção escolhida foi 1, que corresponde à operação de depósito
    if opcao == "1":
        # Solicita o valor do depósito e converte para float
        valor = float(input("Informe o valor do depósito: "))

        # Verifica se o valor é positivo
        if valor > 0:
            # Adiciona o valor ao saldo
            saldo += valor

            # Registra a operação no extrato
            extrato += f"Depósito: R$ {valor:.2f}\n"

            # Confirmação de operação bem-sucedida
            print(f"Depósito no valor de R$ {valor:.2f} realizado com sucesso. Caso deseje realizar outra operação informe abaixo.")
        else:
            # Mensagem de erro caso o valor seja inválido
            print("Operação falhou! O valor informado é inválido.")

    # Verifica se a opção escolhida foi 2, que corresponde à operação de saque
    elif opcao == "2":
        # Solicita o valor do saque
        valor = float(input("Informe o valor do saque: "))

        # Verifica se o valor do saque excede o saldo
        excedeu_saldo = valor > saldo

        # Verifica se o valor do saque excede o limite permitido
        excedeu_limite = valor > limite

        # Verifica se o número de saques já atingiu o limite diário
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        # Caso o saldo seja insuficiente
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        # Caso o valor exceda o limite de saque
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        # Caso o número de saques tenha atingido o limite
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        
        # Caso o valor seja válido e dentro dos limites
        elif valor > 0:
            # Subtrai o valor do saldo
            saldo -= valor

            # Registra a operação no extrato
            extrato += f"Saque: R$ {valor:.2f}\n"

            # Incrementa o contador de saques
            numero_saques += 1
            # Confirmação de operação bem-sucedida
            print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso! Caso deseje realizar outra operação informe abaixo.")

        else:
            # Mensagem de erro para valor inválido
            print("Operação falhou! O valor informado é inválido.")

    # Verifica se a opção é 3, que exibe o extrato
    elif opcao == "3":
        # Exibe o extrato e o saldo atual
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("__________________________________________")

    # Verifica se a opção é 0, que encerra o programa
    elif opcao == "0":
        break

    # Caso o usuário digite uma opção inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    