while True:
    numero_fornecido = int(input("Digite um numero para verificar se é primo: (0 par sair)"))
    if (numero_fornecido % 2 == 0 and numero_fornecido != 0):
        print("O numero é primo")
    if (numero_fornecido % 2 != 0):
        print("O numero não é primo")
    if (numero_fornecido == 0):
        print("Finalizado")
        break

