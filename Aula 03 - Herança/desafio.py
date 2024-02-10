class Calculadora:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=a

        def somar(self):
            return self.a + self.b
        def subtrair(self):
            return self.a - self.b
        def multiplicar(self):
            return self.a * self.b
        def somar(self):
            return self.a / self.b

primeiro_numero = input("digite o primeiro numero:")
segundo_numero = input("digite o segundo numero:")

calc = Calculadora(primeiro_numero,segundo_numero)
print(calc.somar())
print(calc.subtrair())
print(calc.dividir())
print(calc.multiplicar())