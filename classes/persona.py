class Persona:
    def __init__(self) :
        self.__nombre = None
        self.__edad = None
        self.__telefono = None
        self.__direccion = None
        self.__correo = None

    @property
    def nombre(self) :
        return self.__nombre 
    
    @property
    def telefono(self) :
        return self.__telefono

    @property
    def edad(self) :
        return self.__edad
    
    @property
    def direccion(self) :
        return self.__direccion
    
    @nombre.setter
    def nombre(self, nombre) :
        self.__nombre = nombre
    
    @telefono.setter
    def telefono(self, telefono) :
        self.__telefono = telefono
    
    @edad.setter
    def edad(self, edad) :
        self.__edad = edad
   
    @direccion.setter
    def direccion(self, direccion) :
        self.__direccion = direccion

def saludar(self) :
    print(f"Hola, soy {self.nombre}")
    