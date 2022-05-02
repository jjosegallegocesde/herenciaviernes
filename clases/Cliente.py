from select import select
from clases.Persona import Persona

class Cliente(Persona):
    def __init__(self):
        self.__saldo=None
    
    @property
    def saldo(self):
        self.saldo=None
    
    @saldo.setter
    def saldo(self,saldo):
        self.__saldo=saldo

    def mostrarSaldo(self):
        print(self.saldo)

    

    