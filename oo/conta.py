class Conta:

    def __init__(self, numero, titular, saldo, limite) -> None:
        print("Construindo objeto...")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Olá {} seu saldo é {}".format(self.titular, self.saldo))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor
