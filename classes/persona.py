class Persona:
    def __init__(self):
        self._nombre=None
        self._edad=None
        self._telefono=None
        self._direccion=None
        self._correo=None

    @property
    def nombre(self):
        return self._nombre
    @property
    def edad(self):
        return self._edad
    @property
    def telefono(self):
        return self._telefono
    @property
    
    def direccion(self):
        return self._direccion
    @property
    
    def correo(self):
        return self._correo
    
    @nombre.setter
    def nombre (self,nombre):
        self._nombre=nombre
    @edad.setter
    def edad (self,edad):
        self._edad=edad
    @telefono.setter
    def telefono(self,telefono):
        self._telefono=telefono
    @direccion.setter
    def direccion(self, direccion):
        self._direccion=direccion
    @correo.setter
    def correo(self,correo):
        self._correo=correo
    
    def saludar(self):
        print(f"hola yo soy {self.nombre}")