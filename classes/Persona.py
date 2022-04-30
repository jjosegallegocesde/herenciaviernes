class Persona: 

    def __init__(self):
        self.__nombre=None
        self.__edad=None
        self.__telefono=None
        self.__direccion=None
        self.__correo=None

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
    def nombre(self, nombre):
        self.__nombre=nombre

    @edad.setter
    def edad(self, edad):
        self.__nombre=edad

    @telefono.setter
    def telefono(self, telefono):
        self.__nombre=telefono

    @direccion.setter
    def telefono(self, direccion):
        self.__nombre=direccion

    @correo.setter
    def telefono(self, correo):
        self.__nombre=correo
    
    def saludar(self):
        print(f"Hola yo soy {self.nombre}")