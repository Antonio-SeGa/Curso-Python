import random
def lanzar_dados():
    dado1 = random.randint(1, 6)  
    dado2 = random.randint(1, 6)
    return dado1, dado2
    
def evaluar_jugada(dado1,dado2):
    suma = dado1 + dado2
    if suma <= 6:
        return f"La suma de tus dados es {suma}. Lamentable"
    elif 6 <  suma < 10:
        return f"La suma de tus dados es {suma}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma}. Parece una jugada ganadora"

dado1, dado2 = lanzar_dados()
mensaje = evaluar_jugada(dado1,dado2)
print(mensaje)


##################################################

def reducir_lista(lista):
    # Eliminar duplicados convirtiendo la lista en un conjunto
    lista_sin_dup = list(set(lista))
    # Eliminar el valor más alto
    lista_sin_dup.remove(max(lista_sin_dup))
    return lista_sin_dup
    
def promedio(lista_reducida):
    # Calcular el promedio usando sum() y len()
    return sum(lista_reducida) / len(lista_reducida)
    
lista_numeros = [1,2,15,7,2]
lista_reducida = reducir_lista(lista_numeros)
promedio_lista = promedio(lista_reducida)
print(lista_reducida)
print(promedio_lista)



###############################################

def lanzar_moneda():
    return random.choice(["Cara","Cruz"])
    
def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista
        
lista_numeros = [7,2,8,9]
resultado_moneda = lanzar_moneda()
lista_resultante = probar_suerte(resultado_moneda,lista_numeros)
print(lista_resultante)


