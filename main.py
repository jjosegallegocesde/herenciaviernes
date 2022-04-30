#Herencia en python
from classes.Persona import Persona

class Carro(Persona):
    def __init__(self):
        self.__placa=None

    #Getters
    @property
    def placa(self):
        return self.__placa
    
    #Setters
    @placa.setter
    def placa(self,placa):
        self.__placa=placa