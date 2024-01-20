# orientação a objeto em python

class Automovel:
    def __init__(self, cor, modelo, numero_de_portas, tipo_de_cambio,motor, placa):

    # toda classe precisa da função init
        self.cor = cor
        self.modelo = modelo
        self.numero_de_portas = numero_de_portas
        self.tipo_de_cambio = tipo_de_cambio
        self.motor = False
        self.placa = placa

    def liga(self):
        if (self.motor == True):
            print("Carro ja esta ligado")
        else:
            self.motor = True
            print("Carro ligado") 


    def desliga(self):
        self.motor = False
        print("Carro desligado") 

carro1 = Automovel("Prata","Corsinha","2","Manual","GDBX123","GM")

print(carro1.motor)
carro1.liga()
print(carro1.motor)
carro1.liga()
carro1.desliga()
print(carro1.motor)


    
