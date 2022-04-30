class Persona:
    #Contructor
    def __init__(self):
        self.__nombre=None
        self.__edad=0
        self.__telefono=None
        self.__direccion=None
        self.__correo=None

        # Metodos GETTERS 
    @property
    def nombre(self):
        return(self.__nombre)

    @property
    def edad(self):
        return(self.__edad)

    @property
    def telefono(self):
        return(self.__telefono)
    
    @property
    def direccion(self):
        return(self.__direccion)
    
    @property
    def correo(self):
        return(self.__correo)


    #Estos son los SETTERS
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    
    @edad.setter
    def edad(self,edad):
        if(edad < 0):
            print("La edad no es correcta")
        else:
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


    # Otros Metodos o podriamos comparar o decir que son funciones
    def saludar(self):
        print("Cordial saludo para todos")


    
    

    