# simulando um crud atraves de classes

class Pessoas:

    contador = 0
    pessoas = []

    def __init__(self, nome, data_nascimento, cpf, filiacao_um, filiacao_dois):
        self.id = None
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.filiacao_um = filiacao_um
        self.filiacao_dois = filiacao_dois 


    def salvar(self):
        self.__class__.contador += 1
        self.id = self.__class__.contador
        self.pessoas.append(self)

    # essa função formatada os dados
    def __repr__(self):
        return "ID: {}, Nome: {}, Data de Nascimento: {}, CPF: {}, Filiação 1 : {}, Filiação 2 : {}\n".format(self.id, self.nome, self.data_nascimento, self.cpf, self.filiacao_um, self.filiacao_dois)
    
    @classmethod
    # o classmethod pega um padrao dentro da classe
    def listar(cls):
        # o cls serve para pegar tudo que tem dentro da classe
        return cls.pessoas
    
escolha_usuario = int(input("O que deseja: \n1 - Cadastrar, \n2 - Listar , \n3 - Parar"))

while escolha_usuario != 3:

    if escolha_usuario == 1:
        nome = input("Digite um nome: ")
        data_nascimento = input("Digite uma data de nascimento: ")
        cpf = input("Digite o CPF: ")
        filiacao_um = input("Digite uma filiação: ")
        filiacao_dois = input("Digite outra filiação: ")
        nova_pessoa = Pessoas (nome, data_nascimento, cpf, filiacao_um, filiacao_dois)
        nova_pessoa.salvar()
        print("Cadastrado")
        escolha_usuario = int(input("O que deseja: 1 - Cadastrar, 2 - Listar , 3 - Parar"))


    if escolha_usuario == 2:
        print(Pessoas.listar())
        escolha_usuario = int(input("O que deseja: 1 - Cadastrar, 2 - Listar , 3 - Parar"))


    if escolha_usuario == 3:
        break

    if escolha_usuario > 3:
        print("Escolha invalida!!!")

    

    