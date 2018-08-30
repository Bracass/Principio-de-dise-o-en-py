# Principio-de-dise-o-en-py
En los siguientes programas ejemplificamos los princios (DIP y YAGNI)

##Principio DIP
class Corazon (object):
    def __init__(self):
        pass
    def bombearSangre(self):
        pass
    def getLatidos(self):
        NoLatido = 85
        return NoLatido

class Humano (object):
    def __init__(self,corazon):
        self._corazon = corazon

    def getCantidadLatidos(self):
        return self._corazon.getLatidos()

a = Humano(Corazon())
print (a.getCantidadLatidos()) 
        
