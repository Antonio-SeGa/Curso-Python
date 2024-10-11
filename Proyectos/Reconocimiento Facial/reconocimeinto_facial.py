import face_recognition as fr
import cv2

# Cargar imagen
foto_control = fr.load_image_file(r'C:\Users\antos\Downloads\MiFoto.jpg')
foto_prueba = fr.load_image_file(r'C:\Users\antos\Pictures\Antonio_Serrano_Garcia.jpg')

# Pasar imagenes a RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Localizar cara control
lugar_cara = fr.face_locations(foto_control)[0]
cara_codificada = fr.face_encodings(foto_control)[0]

lugar_cara_P = fr.face_locations(foto_prueba)[0]
cara_codificada_P = fr.face_encodings(foto_prueba)[0]


# Mostrar rectangulo
cv2.rectangle(foto_control,
              (lugar_cara[3], lugar_cara[0]),
              (lugar_cara[1], lugar_cara[2]),
              (0,255,0),
              2)

cv2.rectangle(foto_prueba,
              (lugar_cara_P[3], lugar_cara_P[0]),
              (lugar_cara_P[1], lugar_cara_P[2]),
              (0,255,0),
              2)

# Realizar comparacion
resultado = fr.compare_faces([cara_codificada], cara_codificada_P)

# Medida de la distancia
distancia = fr.face_distance([cara_codificada],cara_codificada_P)

# Mostrar resultado
cv2.putText(foto_prueba,
            f'{resultado} {distancia.round(2)}',
            (50,50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0,255,0),
            2)

# Mostrar imagenes
cv2.imshow('foto control', foto_control)
cv2.imshow('foto prueba', foto_prueba)

# Mantener el programa abierto 
cv2.waitKey(0)