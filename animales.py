class Animal:
    def __init__(self,pelos,dientes):
        self.pelos=pelos
        self.dientes=dientes                      
        print ("Se creo animal")
"""
Se crea una clase Animal que posteriormente herede sus objetos
"""
##
"""class Perro(Animal):
    def woof(self):
        print ("Ladrar")"""
##YAGNI 
"""
class Gato(perro):
    def miau(self):
        print ("Soy un gato miau")
"""

##En este caso la clase perro ejemplifica el principio YAGNI, no es necesaria su implementacion

class Gato(Animal):
    def miau(self):
        print ("Soy un gato miau")

liro = Gato("largos","filosos")
liro.miau()

