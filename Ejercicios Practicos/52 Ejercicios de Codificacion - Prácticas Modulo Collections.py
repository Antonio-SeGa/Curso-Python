from collections import Counter, defaultdict, deque

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
contador = Counter(lista)
print(contador)


################################

mi_diccionario = defaultdict(lambda:"Valor no hallado")
mi_diccionario["edad"] = 44
print(mi_diccionario["nombre"])



##############################

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
lista_ciudades.appendleft("Mexico")
print(lista_ciudades)