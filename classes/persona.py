class persona:
    #constructor
    def __init__(self):
        #atributos
        self.__nombre=None 
        self.__telefono=None 
        self.__direccion=None 
        self.__correo=None
        self.__edad=None

    #metodos get, obtener el valor de un atributo
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
    

#metodos set (escribr/ingresas/llevar un valor a un atributo)
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @edad.setter
    def edad(self,edad):
        if(edad<0):
            print("No acepto edades negativas")
        else:
            self.__edad=edad

    @direccion.setter
    def direccion(self,direccion):
        self.__direccion=direccion

    @telefono.setter
    def telefono(self,telefono):
        self.__telefono=telefono

    @correo.setter
    def correo(self,correo):
        self.__correo=correo