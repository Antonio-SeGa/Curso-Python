palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for dato in [palabra, lista, tupla]:
    print(len(dato))


#########################
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
        
mago1 = Mago()
arquero1 = Arquero()
samurai1 = Samurai()

personajes = [arquero1,mago1,samurai1]

for personaje in personajes:
    personaje.atacar()


#########################
class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

def personaje_defender(personaje):
    personaje.defender()
    
mago1 = Mago()
personaje_defender(mago1)