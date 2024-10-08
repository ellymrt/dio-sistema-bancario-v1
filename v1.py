menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo = saldo + valor
            extrato = extrato + f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Não foi possível realizar o depósito.")

    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Não foi possível realizar o saque, saldo suficiente.")

        elif excedeu_limite:
            print("Não foi possível realizar o saque, valor informado não está no limite.")

        elif excedeu_saques:
            print("Não foi possível realizar o saque, você já realizou o numero máximo de saques.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Valor informado é inválido!")

    elif opcao == "e":
        print("\nExtrato")
        print("Não teve movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Opção inválida, selecione novamente.")