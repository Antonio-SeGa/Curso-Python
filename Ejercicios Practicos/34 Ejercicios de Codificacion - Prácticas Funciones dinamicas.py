lista_numeros = [7,-8,10]
def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False
        else:
            pass
    return True
    
    #return all(num > 0 for num in lista)


#################################################################
# Crear la lista con valores de ejemplo
lista_numeros = [120, 1500, -45, 999, 500, 0, 350, 1001]
# Definir la función suma_menores
def suma_menores(lista_numeros):
    suma=0
    for numero in lista_numeros:
        if numero in range(1,1000):
            suma += numero
        else:
            pass
    return suma
    # Sumar los números que cumplan con la condición (> 0 y < 1000)
    #return sum(num for num in lista if 0 < num < 1000)




######################################################
lista_numeros = [1,50,502,5000,755,600,33,61]
def cantidad_pares(lista_numeros):
    cantidad=0
    for numero in lista_numeros:
        if numero % 2 == 0:
            cantidad += 1
        else:
            pass
    return cantidad
    #return sum(1 for num in lista if num % 2 == 0)

contar = cantidad_pares(lista_numeros)
print(contar)