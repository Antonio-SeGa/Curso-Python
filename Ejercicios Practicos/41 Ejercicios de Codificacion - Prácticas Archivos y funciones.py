def abrir_leer(archivo):
    archivo = open(archivo)
    return archivo.read()


######################
def sobrescribir(archivo):
    archivo_sobrescribir = open(archivo, "w")
    archivo_sobrescribir.write("contenido eliminado")
    archivo_sobrescribir.close()

#######################
def registro_error(archivo):
    archivo_registro = open(archivo, "a")
    archivo_registro.write("se ha registrado un error de ejecución")
    archivo_registro.close()