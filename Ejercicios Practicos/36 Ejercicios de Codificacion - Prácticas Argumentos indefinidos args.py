def suma_cuadrados(*args):
    return sum(pow(arg,2) for arg in args)
    
suma = suma_cuadrados(1,2,3)
print(suma)

####################################
def suma_absolutos(*args):
    suma = 0
    for arg in args:
        suma += abs(arg)
    
    return suma
    # return sum(abs(arg) for arg in args)
    
suma = suma_absolutos(1,-2,3,-4)
print(suma)

####################################
def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f"{nombre}, la suma de tus números es {suma_numeros}"
    
print(numeros_persona("Juan", 1, 2, 3)) 