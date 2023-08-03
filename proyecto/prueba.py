#Para probar los codigos

from paquete.mod_val import valInt, valFloat, valComplex, valList
from paquete import multiplicar, gauss_jordan, transponer, producto, resolver_sistema, determinante
from paquete.mod_crypto import encriptar, desencriptar

# PARA EL MODULO VALIDACIÓN
    #ValInt()

numero=4
arreglo=[4,10]
print("VALIDACIÓN INT:", valInt(numero,arreglo))
    
    #Valfloat()

numero=4.4
arreglo=[4, 10]
print("VALIDACIÓN FLOAT:", valFloat(numero, arreglo))

   #ValComplex()

numero=3+4j
arreglo=(4,10) 
print("VALIDACIÓN COMPLEX:", valComplex(numero, arreglo))

   #ValList()

print("VALIDACIÓN LIST:", valList([1, 2, 3], 3, 'len'),"\n")

#PARA EL MODULO DE ALGEBRA
    #MULTIPLICACIÓN DE MATRICES
matriz_a = [[16, 24, 12], [6, 33, 9]]
matriz_b = [[20, 4], [0, 63], [25, 44]]
matriz_resultante = multiplicar(matriz_a, matriz_b)
print("La matriz resultante entre la matriz A y matriz B es: ")
if matriz_resultante is not None:
    for valor in matriz_resultante:
        print(valor)
else:
    print("No se pudo realizar la multiplicación\n")
    print("\n")

    #INVERSION DE MATRICES
matriz=[[2, 3, 4], [5, 6, 7], [8, 9, 11]]
matriz_resultante=gauss_jordan(matriz)
if type(matriz_resultante) == list:
  matriz_redondeada = [[round(float(x), 1) for x in fila] for fila in matriz_resultante]
  print("La inversa de la matriz es:")
  for valor in matriz_redondeada:
    print(valor)
else:
  print(matriz_resultante)

    #TRANSPOSICIÓN DE MATRICES
matriz= [[20, 4, 12], [0, 63, 4], [25, 44, 10]]
transpuesta=transponer(matriz)
print("\nLa transpuesta de la matriz es:")
for valor in transpuesta:
    print(valor)

    #PRODUCTO VECTORIAL
vector_a = [1, 2, 3]
vector_b = [4, 5, 7]
vector_resultante= producto(vector_a, vector_b)
if vector_resultante is not None:
    print("\nEl vector resultante entre el vector A y vector B es: ", vector_resultante)
else:
    print("No se pudo realizar el producto vectorial\n")

    #SISTEMA DE ECUACIONES
matriz=[[2, 3, 4], [5, 7, 6], [56, 7, 9]]
vector=[[1], [2], [3]]
resultado=resolver_sistema(matriz, vector)
print("\nLa solución del sistema de ecuaciones es:", resultado)

    #DETERMINANTE
matriz=[[2, 3, 4], [12, 7, 5], [56, 7, 0]]
matriz_resultante=determinante(matriz)
print("\nEl determinante de la matriz es:", matriz_resultante)

#PARA EL MODULO DE INCRIPTACIÓN

encriptacion_key = {"a": "j", "b": "*", "c": "%", "d": "¿", "e": "?", "f": "!", "g":"@", "h": "c", "i": "#", "j": "$", "k": "°", "l": "a", "m": "h", "n": "x", "ñ": "+", "o": "-", "p": "^", "q": "<", "r": "w", "s": "t", "t":">", "u": "|", "v": "k", "w": "~", "x": ";", "y": "¬", "z": "z", " ": "_", "A": "j", "B": "*", "C": "%", "D": "¿", "E": "?", "F": "!", "G":"@", "H": "c", "I": "#", "J": "$", "K": "°", "L": "a", "M": "h", "N": "x", "Ñ": "+", "O": "-", "P": "^", "Q": "<", "R": "w", "S": "t", "T":">", "U": "|", "V": "k", "W": "~", "X": ";", "Y": "¬", "Z": "z", " ": "_"} 
mensaje=input("\nEscriba un mensaje:")
encriptacion_mensaje = encriptar(mensaje, encriptacion_key)
print("Mensaje encriptado:", encriptacion_mensaje)
desencriptar_mensaje = desencriptar(encriptacion_mensaje, encriptacion_key)
print("Mensaje desencriptado:", desencriptar_mensaje)
print("\nGracias por usar el programa. ¡Hasta pronto!")