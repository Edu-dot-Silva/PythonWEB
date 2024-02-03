saldo = 100

cheque_especial = saldo * 0.50

while (saldo != (saldo + cheque_especial)):
    print("Saldo: R$",saldo, "\nValor de cheque especial: R$",cheque_especial)
    saque = float(input("Valor de saque:"))

    if (saque > saldo):
        diferenca = cheque_especial - (saque-saldo)
        print("Você usou seu cheque especial com R$ ",diferenca)
        saldo = saldo - saque
        cheque_especial = cheque_especial - diferenca

# verificar erro depois
