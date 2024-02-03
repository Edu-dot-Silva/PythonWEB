numero_secreto = 82

total_tentativas = 3

for rodada in range(1,total_tentativas + 1):
    print("\nTentativa {:02d} de {:02d}".format(rodada,total_tentativas))

    tentativa = input("Tente acertar o numero de 1 a 100:")
    print("Você digitou ",tentativa)

    tentativa_int = int(tentativa)

    if (tentativa_int < 1 or tentativa_int > 100):
        print("Tentativa Invalida, somente numeros entre 0 e 100")

    acerto= tentativa_int == numero_secreto

    if (acerto):
        print("Acertou")
        break
    else:
        print("Errou")