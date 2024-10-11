import cv2
import face_recognition as fr
import os
import numpy
import time
from datetime import datetime

# Crear base de datos en listas
ruta = 'Proyectos\\Reconocimiento Facial\\empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(rf'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

print(nombres_empleados)

# Codificar imagenes
def codificar(imagenes):
    # Crear lista nueva
    lista_codificada = []
    # Pasar imagenes a RGB
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        # codificar
        codificado = fr.face_encodings(imagen)[0]

        # Agregar a la lista
        lista_codificada.append(codificado)
    # Devolver lista codificada
    return lista_codificada

# Registrar ingresos
def registrar_ingreso(persona):
    f  = open('Proyectos\\Reconocimiento Facial\\registro.csv', 'r+')
    lista_datos = f.readlines()
    nombre_registr0 = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombre_registr0.append(ingreso[0])
    
    if persona not in nombre_registr0:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')

lista_empleados_codificados = codificar(mis_imagenes)

# tomar una imagen de camara web
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Esperar unos segundos para que la cámara se estabilice y pueda tomar la foto
time.sleep(2)

# Leer imagen de la camara
exito, imagen = captura.read()

# Liberar los recursos de la cámara
captura.release()

if not exito:
    print("No se ha podido tomar la captura")
else:
    # Reconocer cara en captura
    cara_captura = fr.face_locations(imagen)

    # codificar cara captura
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    # Buscar coincidencias
    for caracodif, caraubica in zip(cara_captura_codificada,cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificados,caracodif)
        distancias = fr.face_distance(lista_empleados_codificados,caracodif)
        
        print(distancias)

        indice_coincidencia = numpy.argmin(distancias)

        # Mostrar coincidencias
        if distancias[indice_coincidencia] > 0.6:
            print("No hay coincidencias")
        else:
            # Buscar el nombre del empleado 
            nombre = nombres_empleados[indice_coincidencia]

            y1, x2, y2, x1 = caraubica
            cv2.rectangle(imagen,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(imagen,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(imagen,nombre,(x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)

            registrar_ingreso(nombre)

            # Mostrar la imagen obtenida
            cv2.imshow('Imagen web', imagen)

            # Mantener imagen 
            cv2.waitKey(0)
