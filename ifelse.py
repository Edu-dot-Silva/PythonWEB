# numero = int(input("Digite um numero:"))

# NUM = 32

# if numero == NUM:
#     print("Acertou!!!")
# else:
#     print("Errou")

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
nota4 = float(input("Digite a quarta nota:"))

media = (nota1+nota2+nota3+nota4)/4

if (media >= 7):
    print("Aluno Aprovado com média {:,.1f}".format(media))

if (media >= 4) and (media <= 6):
    print("Aluno em Recuperação com média {:,.1f}".format(media))

if (media < 4):
    print("Aluno Reprovado com média {:,.1f}".format(media))

if (media > 10):
    print("Média Invalida")
        

