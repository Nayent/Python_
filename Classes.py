

class Conta:

    def __init__(self, numero, titular, saldo, limite):    ##Função construtora // Self -> Refenria de armazenamento
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"O saldo do titular {self.__titular} é de {self.__saldo}")

    def deposita(self, valor):
        self.__saldo += valor

    def saque(self,valor):
        self.__saldo -=valor

    def transferir(self,valor,recebedor):
        self.saque(valor)
        recebedor.deposita(valor)




'''
import os
clear = lambda: os.system('cls')
'''