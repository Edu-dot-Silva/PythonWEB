# classe pai

class Animal:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return f"O {self.nome} esta falando!"
        # f(format) para template string
        # se colocar só print na execução ira aparecer um none que diz que a função esta retornando vazio
        # para resolver só colocar um return que explicita oq sera retornado

# classe filha
        
# primeira classe com herança
class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca
    
    def latir(self):
        return f"O {self.nome} esta latindo!"

# segunda classe com herança
class Cobra(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.tipo_de_pele = ("Lisa","Áspera", "Opaca", "Brilhante")

    def rastejar(self):
        return f"O {self.nome} esta rastejando!"
        
# pode criar a o objeto filho que ja puxa informaçoes do pai
cachorro_um = Cachorro("Rex",6,"Golden Retriver")

print("Infos do cachorro puxados da classe pai:")
print(cachorro_um.nome)
print(cachorro_um.idade)
print(cachorro_um.raca)
print(cachorro_um.falar())
# puxando infos do pai


print("\nInfos do cachorro puxados da classe Filha:")
print(cachorro_um.nome)
print(cachorro_um.latir())
# puxando infos da filha

cobra_um = Cobra("Zé",10)

print("\nInfos da cobra:")
print(cobra_um.nome)
print(cobra_um.idade)
print(cobra_um.tipo_de_pele[2])
print(cobra_um.rastejar())
