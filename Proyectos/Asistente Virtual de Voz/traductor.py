import pyttsx3
from googletrans import Translator
from langdetect import detect

id_voice1 = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id_voice2 = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
id_voice3 = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"


# Inicializar el traductor y el motor de texto a voz
traductor = Translator()
engine = pyttsx3.init()

# Función para traducir y hablar
def traducir_y_hablar(texto):
    # Detectar el idioma del texto
    idioma_detectado = detect(texto)

    # Definir idioma de destino según el idioma detectado
    if idioma_detectado == 'es':
        idioma_destino = 'en'  # Traducir a inglés si está en español
        print(f"Texto detectado en español, traduciendo a inglés...")
    elif idioma_detectado == 'en':
        idioma_destino = 'es'  # Traducir a español si está en inglés
        print(f"Texto detectado en inglés, traduciendo a español...")
    else:
        print(f"Idioma no soportado: {idioma_detectado}")
        return

    # Traducir el texto
    traduccion = traductor.translate(texto, dest=idioma_destino).text
    print(f"Traducción: {traduccion}")

    # Configurar el motor de voz para el idioma de destino
    if idioma_destino == 'en':
        engine.setProperty('voice', id_voice3)  # Voz en inglés
    else:
        engine.setProperty('voice', id_voice1)  # Voz en español
    
    # Leer en voz alta la traducción
    engine.say(traduccion)
    engine.runAndWait()

