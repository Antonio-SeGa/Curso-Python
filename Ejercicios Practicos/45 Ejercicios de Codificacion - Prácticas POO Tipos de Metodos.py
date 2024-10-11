# Metodo statico
class Mascota():
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")
        
Mascota.respirar()


# Metodo de clase
class Jugador():
    vivo = False
    
    @classmethod
    def revivir(cls):
        cls.vivo = True

#####
class Personaje():
    
    def __init__(slef,cantidad_flechas):
        slef.cantidad_flechas = cantidad_flechas
        
    def lanzar_flecha(slef):
        slef.cantidad_flechas = slef.cantidad_flechas - 1

        
        