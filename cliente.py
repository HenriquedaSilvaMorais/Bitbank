class Cliente:
    def __init__(self,numero,saldo):

        self.numero = numero
        self.saldo = saldo

    def Sacar(self,valor):
        self.saldo -= valor
        print("Vocé sacou R$: {}".format(self.valor))

    def Depositar(self,valor):
        self.saldo += valor
        print("Vocé depositou {}".format(self.valor))

    def Trasfirir(self,destino,valor):
        self.saldo = self.saldo -valor
        destino.saldo = destino.saldo + valor
        print("Voce trasfiriu {} para {}".format(valor,destino.nome))

    def Extrato(self):
        print("Ola {} seu saldo e de {}".format(self.nome,self.saldo))

    def get_saldo(self):
        return self.saldo
    def set_saldo(self,valor):
        self.saldo = valor