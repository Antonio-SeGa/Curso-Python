texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
# Utilizamos lstrip() para eliminar los caracteres especificados desde la izquierda
resultado = texto.lstrip(",:%_#")
print(resultado)


frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 
frutas.insert(3,"naranja")
print(frutas)



marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)