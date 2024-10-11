class Persona:
    def __init__(slef, nombre, edad):
        slef.nombre = nombre
        slef.edad = edad

class Alumno(Persona):
    pass


########################
class Mascota:
    def __init__(slef, edad, nombre, cantidad_patas):
        slef.edad = edad
        slef.nombre = nombre
        slef.cantidad_patas = cantidad_patas
        
class Perro(Mascota):
    pass


#####################
class Vehiculo:
    
    def acelerar(slef):
        pass
    
    def frenar(slef):
        pass
    
class Automovil(Vehiculo):
    pass