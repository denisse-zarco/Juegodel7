import random

class Dado:
    def __init__(self):
        self.valor = 0

    def tirarDado(self):
        self.valor = random.randin(1, 6)

    def getValor(self):
        return self.valor
