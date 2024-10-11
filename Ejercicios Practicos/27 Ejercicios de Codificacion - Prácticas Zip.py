capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
for capital, pais in list(zip(capitales,paises)):
    #print(f"La capital de {pais} es {capital}")
    pass


marcas = {"nike","puma","adidas"}
productos = {"tenis","guantes","playera"}
mi_zip = list(zip(marcas,productos))
#print(mi_zip)



numeros_espanol = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
numeros_portugues = ['um', 'dois', 'três', 'quatro', 'cinco']
numeros_ingles = ['one', 'two', 'three', 'four', 'five']
numeros = list(zip(numeros_espanol, numeros_portugues, numeros_ingles))
print(numeros)
