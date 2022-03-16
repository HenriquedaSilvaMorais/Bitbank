class Banco:

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade


    def Imprimir(self,arquivo):
        print("Nome: {}".format(self.nome))
        print("Idade: {}".format(self.idade))
        print("Numero: {}".format(arquivo.numero))
        print("Saldo: {}".format(arquivo.saldo))
