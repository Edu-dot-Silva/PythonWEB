class Filme:
    def __init__(self,nome ,genero, duracao, diretor):

        self.nome = nome
        self.genero = genero
        self.duracao = duracao
        self.diretor = diretor

print("*****************")
print("Central de Filmes")
print("*****************\n")

print("Cadastre um filme")

nome_digitado = input("Digite o nome do filme:")
genero_digitado = input("Digite o genero do filme:")
duracao_digitada = input("Digite a duração em minutos:")
diretor_digitado = input("Digite o nome do diretor do Filme:")

filme_cadastrado = Filme(
nome_digitado,
genero_digitado,
duracao_digitada,
diretor_digitado
)

print(filme_cadastrado.nome)
print(filme_cadastrado.genero)
print(filme_cadastrado.duracao ,"Minutos")
print(filme_cadastrado.diretor)


