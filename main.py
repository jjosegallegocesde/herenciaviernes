#Herencia en python
from classes.Persona import Persona

#Objeto
mi_nombre=Persona()


#Utlizo el Setter
mi_nombre.nombre="Edisson Alexander"
mi_nombre.edad=42
mi_nombre.telefono="3008889900"
mi_nombre.direccion="carrer 39 sin fin"
mi_nombre.correo="edisson320@yahoo.es"




#Acceder a los atributos
print(mi_nombre.nombre) 
print(mi_nombre.edad)
print(mi_nombre.telefono)
print(mi_nombre.direccion)
print(mi_nombre.correo)



