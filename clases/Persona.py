class Persona:

	 #creamos el constructor de la clase
	def __init__(self):
		self.__nombre = None
		self.__edad = None
		self.__telefono = None
		self.__direccion = None
		self.__correo = None

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
	
	@nombre.setter
	def nombre(self,nombre):
		self.__nombre =nombre

	@nombre.setter
	def edad(self,edad):
		self.__edad =edad

	@nombre.setter
	def telefono(self,telefono):
		self.__telefono =telefono

	@nombre.setter
	def telefono(self,telefono):
		self.__telefono =telefono
	
	@nombre.setter
	def direccion(self,direccion):
		self.__direccion =direccion

	@nombre.setter
	def correo(self,correo):
		self.__correo =correo
	
	def clasificar(self,nombre):
		print(f"Hola mi nombre es {nombre}")

		
	 
