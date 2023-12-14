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

    inicio_contraseña = []
    if numeros:
        inicio_contraseña.append(random.choice(string.digits))
    if caracteres_especiales:
        inicio_contraseña.append(random.choice(string.punctuation))
    random.shuffle(inicio_contraseña)
    
    longitud_restante = longitud - len(inicio_contraseña)
    contraseña_restante = ''.join(random.choice(caracteres) for i in range(longitud_restante))
    contra_final = ''.join(inicio_contraseña) + contraseña_restante
    
    return contra_final

resultado = generar_contraseña()
print("Contraseña generada:", resultado.replace(",","").replace(".",""))
