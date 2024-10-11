def cantidad_atributos(**kwargs):
    cantidad = 0
    for clave in kwargs.items():
        cantidad += 1
    return cantidad
    #return len(kwargs)
    
cantidad = cantidad_atributos(x=1,y=2)
print(cantidad)

####################################################

def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    #return list(kwargs.values())
    return lista
    
valores = lista_atributos(x=1,y=2,z=3)
print(valores)


####################################################
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')