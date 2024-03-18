menu = """
[d] Depósito
[s] Saque
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
        valor_deposito = float(input("Digite o valor do depósito: "))
        saldo += valor_deposito
        print(f"Depósito de R$ {valor_deposito} realizado. Saldo atual: R$ {saldo:.2f}")
        
    elif  opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            saque = float(input("Valor do saque: "))
            if (saldo - saque) >= 0:
                saldo -= saque
                extrato += f"\nSaque de R$ {saque}"
                numero_saques += 1
                print(f"Saque de R$ {saque} realizado. Saldo atual: R$ {saldo:.2f}")
            else:
                print("Saldo Insuficiente!")
        else:
            print("Você atingiu o limite de saques do dia")
    
    elif opcao == "e":
        print("Extrato")
        print(extrato)
    
    elif opcao == "q":
        break
    
    else:
        print("Opção Inválida, selecione novamente uma operação válida")
