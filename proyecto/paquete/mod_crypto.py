#Función para incriptar

def encriptar(mensaje, encriptacion_key):
    encriptacion_mensaje = ""
    for char in mensaje:#Con este bucle, verificamos si el caracter est presente en el diccionario de encriptacion_key. Si es asi se agrega 
# el caracter encriptido correspondiente a la variable
        if char in encriptacion_key:
            encriptacion_mensaje += encriptacion_key[char]
        else:
            encriptacion_mensaje += char
    return encriptacion_mensaje


def desencriptar(encriptacion_mensaje, encriptacion_key):
    desencriptar_key = {value: key for key, value in encriptacion_key.items()} #Se utiliza para crear un nuevo diccionario, este diccionario 
#se crea a partir de un diccionario encriptar_key. Este diccionario se crea apatir de diccionario encriptacion_key utilizando la funcion 
# encriptar, pero invierte los pares clave-valor
    desencriptar_mensaje = ""
    for char in encriptacion_mensaje:
        if char in desencriptar_key:
            desencriptar_mensaje += desencriptar_key[char]
        else:
            desencriptar_mensaje += char
    return desencriptar_mensaje