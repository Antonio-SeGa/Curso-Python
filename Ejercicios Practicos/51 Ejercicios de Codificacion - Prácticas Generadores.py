def secuencia_infinita():
    num = 0
    while True:
        num += 1
        yield num
 
generador = secuencia_infinita()


###########################################
def multiplos_siete():
    num = 1
    while True:
        yield 7*num
        num += 1
 
generador = multiplos_siete()


###########################################
def mensaje():
    x = "Te quedan 3 vidas"
    yield x
    
    x = "Te quedan 2 vidas"
    yield x
    
    x = "Te queda 1 vida"
    yield x
    
    x = "Game Over"
    yield x
    
perder_vida = mensaje()
