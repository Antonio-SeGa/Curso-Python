class Perro():
    
    def ladrar(self):
        print("Guau!")
        
mi_perro = Perro()
mi_perro.ladrar()

#############################
class Mago():
    
    def lanzar_hechizo(self):
        print("¡Abracadabra!")
        
merlin = Mago()
merlin.lanzar_hechizo()


##################################
class Alarma():
    def postergar(slef, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
        
prueba = Alarma()
prueba.postergar(4)