class Casa():
    
    def __init__(slef,color,cantidad_pisos):
        slef.color = color
        slef.cantidad_pisos = cantidad_pisos
        
casa_blanca = Casa("blanco",4)

##################
class Cubo():
    
    caras = 6
    
    def __init__(slef,color):
        slef.color = color

cubo_rojo = Cubo("rojo")


##############################
class Personaje():
    
    real = False
    
    def __init__(slef, especie, magico, edad):
        slef.especie = especie
        slef.magico = magico
        slef.edad = edad
        
harry_potter = Personaje("Humano", True, 17)