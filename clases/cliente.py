from clases.Persona import Persona

class Cliente(Persona):
    def __init__(self):
        self._saldo=None
    @property 
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self,saldo):
        self._saldo=saldo

    def mostrarSaldo(self):
        print(self.saldo)