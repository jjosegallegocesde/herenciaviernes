

from ctypes import wstring_at


class Persona:

    def _init_(self):
        self.__nombre = None
        self.__edad = None
        self.__direccion = None
        self.__correo = None
    
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dirreccion(self):
        return self.__direccion
    
    @property
    def correo(self):
        return self.__correo


    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre


    @edad.setter
    def edad(self, edad):
        self.__edad=edad

    @dirreccion.setter
    def dirreccion(self, dirreccion):
         self.__direccion=dirreccion

    @correo.setter
    def dirreccion(self, dirreccion):
         self.__direccion=dirreccion


    def saludar (self):
        print(f"hola mi vida {self.nombreg}")

