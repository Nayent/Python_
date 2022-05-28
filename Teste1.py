class conta:
    def __init__(self, numero):
        self.__numero = numero

    @property
    def get_numero(self):
        return self.__numero


teste = conta(123)
print(teste.get_numero)