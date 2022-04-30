from clases.Persona import Persona

class Cliente(Persona):
    def __init__(self):
        self.__saldo=None

    @property
    def saldo(self):
        return self.__saldo    

    @saldo.setter
    def saldo(self,saldo):
        self.__saldo=saldo    

    def mostrarSaldo(self):
        print(self.saldo)

