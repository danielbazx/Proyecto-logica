print("""Bienvenidos al nuestro avance de un generador de contraseña, que incluya numeros y caracteres especiales
      Disfruten :)""")

import random
import string
longitud = int(input("Ingrese la longitud deseada de la contraseña: "))
numeros = input("¿Ingresar números para la contraseña? (Sí/No): ").strip().lower() == "si"
caracteres_especiales = input("¿Ingresar caracteres especiales en la contraseña? (Sí/No): ").strip().lower() == "si"

def generar_contraseña():
    caracteres = string.ascii_letters
    if numeros:
        caracteres += string.digits
    if caracteres_especiales:
        caracteres += string.punctuation

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

contra_final = generar_contraseña()
print("Contraseña generada:", contra_final)
