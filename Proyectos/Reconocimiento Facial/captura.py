import cv2
import time

# Iniciar captura de video desde la cámara
cap = cv2.VideoCapture(0)

# Esperar unos segundos para que la cámara se estabilice
time.sleep(10)

# Leer un frame después de la espera
ret, frame = cap.read()

if ret:
    cv2.imshow('Frame', frame)
    cv2.waitKey(0)

# Liberar los recursos de la cámara
cap.release()
cv2.destroyAllWindows()
