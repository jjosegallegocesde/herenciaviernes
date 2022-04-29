class Persona:
    def __init__ (self):
        self.__nombre=None
        self.__edad=None
        self.__telefono=None
        self.__direccion=None
        self.__correo=None

    def saludar(self):
        print(f"hola yo soy {self.nombre}")

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def telefono(self):
        return self.__telefono
    
    @property
    def direccion(self):
        return self.__direccion

    @property
    def correo(self):
        return self.__correo

    @nombre.setter
    def nombre(self,name):
        self.__name=name
    
    @edad.setter
    def edad(self,edad):
        self.__edad=edad
    
    @telefono.setter
    def telefono(self,telefono):
        self.__telefono=telefono

    @direccion.setter
    def direccion(self,direccion):
        self.__direccion=direccion

    @correo.setter
    def correo(self,correo):
        self.__correo=correo