class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Olá {} seu saldo é {}".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponível_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponível_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} excede o limite".format(valor))

    def transfere(self, valor, destino):
        if(self.__pode_sacar(valor)):
            self.saca(valor)
            destino.deposita(valor)
            print('Você transferiu {} para {}'.format(valor, destino))
        else:
            print("O valor {} excede o limite".format(valor))

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB": "001", "Caixa": "104","Bradesco": "237"}
