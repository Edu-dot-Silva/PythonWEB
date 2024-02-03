# Calculadora

class Calculadora:

    

    
    def soma (a,b):
        print(a + b)    
        
    
    def subtrai ():
        pass

    
    def multiplica ():
        pass

    
    def divide ():
        pass

print ("Calculadora")

def escolhe_primeiro_numero():
    primeiro_numero = int(input("Digite o primeiro numero:"))

def escolhe_segundo_numero():
    segundo_numero = int(input("Digite o segundo numero:"))


escolha_operacao = (input("Qual operação deseja realizar (Ultilize o teclado numerico):"))


if escolha_operacao == "+":

    a = escolhe_primeiro_numero()
    b = escolhe_segundo_numero()

    escolhe_primeiro_numero()
    escolhe_segundo_numero()

    print(Calculadora.soma(a,b))