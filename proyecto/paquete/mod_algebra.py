# Función que multiplique dos matrices

def multiplicar(matriz_a, matriz_b):
  # Obtener las dimensiones de las matrices
  filas_a = len(matriz_a) # Número de filas de A
  columnas_a = len(matriz_a[0]) # Número de columnas de A
  filas_b = len(matriz_b) # Número de filas de B
  columnas_b = len(matriz_b[0]) # Número de columnas de B

  # Verificar que las matrices se puedan multiplicar
  if columnas_a != filas_b:
    print("Las matrices no se pueden multiplicar")
    return None
  
  # Crear una matriz vacía para almacenar el resultado
  matriz_resultante = [[0 for j in range(columnas_b)] for i in range(filas_a)]
  # Esta línea de código utiliza una comprensión de lista anidada para crear una matriz de filas_a filas y columnas_b columnas, 
  # donde cada elemento se inicializa en 0. La comprensión de lista interna ([0 for j in range(columnas_b)]) crea una lista de 
  # columnas_b elementos, todos inicializados en 0. Esta lista se repite filas_a veces para crear la matriz resultante.

  # Realizar la multiplicación usando un bucle anidado
  for i in range(filas_a):
    for j in range(columnas_b):
      for k in range(columnas_a):
        matriz_resultante[i][j] += matriz_a[i][k] * matriz_b[k][j]

  # Devolver la matriz resultante
  return matriz_resultante



#Función para invertir funciones por el metodo de Gauss-Jordan

def gauss_jordan(matriz):
  # Convierte la matriz en una lista de listas
  matriz = [list(fila) for fila in matriz]
  fila = len(matriz)
  columna = len(matriz[0])
  # Verifica si la matriz es cuadrada
  if fila != columna:
    return ("La matriz no es invertible porque no es cuadrada")
  # Crea una matriz identidad del mismo tamaño
  identidad = [[float(i == j) for i in range(fila)] for j in range(fila)]
  # Concatena la matriz original con la identidad
  matriz = [fila_a + fila_b for fila_a, fila_b in zip(matriz, identidad)]
  # Se aplica el método de Gauss-Jordan
  for i in range(fila):
    # Busca el pivote en la columna i
    pivote = matriz[i][i]
    # Si el pivote es cero, busca otra fila que tenga un valor distinto de cero
    if pivote == 0:
      for j in range(i+1, fila):
        if matriz[j][i] != 0:
          # Intercambia las filas i y j
          matriz[i], matriz[j] = matriz[j], matriz[i]
          pivote = matriz[i][i]
          break
    # Si no se encuentra un pivote distinto de cero, la matriz no es invertible
    if pivote == 0:
      return None
    # Divide la fila i por el valor del pivote
    for j in range(2*columna):
      matriz[i][j] /= pivote
    # Resta la fila i multiplicada por el coeficiente adecuado a las demás filas
    for j in range(fila):
      if j != i:
        coeficiente = matriz[j][i]
        for k in range(2*columna):
          matriz[j][k] -= coeficiente * matriz[i][k]
  return [fila[columna:] for fila in matriz]


#Función que calcula el producto vectorial

def producto(vector_a, vector_b):
  # Verificar que los vectores tengan tres componentes
  if len(vector_a) != 3 or len(vector_b) != 3:
    return None
  
  # Calcular el producto vectorial usando la regla del determinante
  componente_x = vector_a[1] * vector_b[2] - vector_a[2] * vector_b[1]
  componente_y = vector_a[2] * vector_b[0] - vector_a[0] * vector_b[2]
  componente_z = vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0]
  # Retornar el vector resultante
  return [componente_x, componente_y, componente_z]



#Función para realizar la transposición de matrices

def transponer(matriz):
  # Crear una matriz vacía con las dimensiones invertidas de la original
  filas = len(matriz)
  columnas = len(matriz[0])
  transpuesta = [[None for i in range(filas)] for j in range(columnas)]

  # Copiar los elementos de la matriz original a la transpuesta intercambiando filas por columnas
  for i in range(filas):
    for j in range(columnas):
      transpuesta[j][i] = matriz[i][j]

  # Retornar la matriz transpuesta
  return transpuesta



# La función que resuelve el sistema de ecuaciones

def resolver_sistema(matriz, vector):
  # Convierte la matriz y el vector en listas de listas
  matriz = [list(fila) for fila in matriz]
  vector = [list(fila) for fila in vector]
  # Obtiene el número de ecuaciones y variables
  ecuaciones = len(matriz)
  variables = len(matriz[0])
  # Verifica que el sistema sea compatible determinado
  if ecuaciones != variables or ecuaciones != len(vector):
    return "La matriz no es cuadrada o el vector no tiene todos los elementos"
  # Concatena la matriz de coeficientes con el vector de términos independientes
  matriz = [fila_a + fila_b for fila_a, fila_b in zip(matriz, vector)] 
  # Aplica el método de Gauss-Jordan para obtener la forma escalonada reducida
  for i in range(ecuaciones):
    # Busca el pivote en la columna i
    pivote = matriz[i][i]
    # Si el pivote es cero, busca otra fila que tenga un valor distinto de cero
    if pivote == 0:
      for j in range(i+1, ecuaciones):
        if matriz[j][i] != 0:
          # Intercambia las filas i y j
          matriz[i], matriz[j] = matriz[j], matriz[i]
          pivote = matriz[i][i]
          break
    # Si no se encuentra un pivote distinto de cero, el sistema no tiene solución única
    if pivote == 0:
      return None
    # Divide la fila i por el valor del pivote
    for j in range(variables+1):
      matriz[i][j] /= pivote
    # Resta la fila i multiplicada por el coeficiente adecuado a las demás filas
    for j in range(ecuaciones):
      if j != i:
        coeficiente = matriz[j][i]
        for k in range(variables+1):
          matriz[j][k] -= coeficiente * matriz[i][k]
  # Retorna la parte derecha de la matriz aumentada, que es el vector solución
  resultado=[fila[variables:] for fila in matriz]
  resultado_redondeado = []
  for fila in resultado:
    fila_redondeada = [round(numero, 4) for numero in fila]
    resultado_redondeado.append(fila_redondeada)
  return resultado_redondeado



#Función que calcula el determinante de la matriz

def determinante(matriz):
  # Convierte la matriz en una lista de listas
  matriz = [list(fila) for fila in matriz]
  # Obtiene el número de filas y columnas
  filas = len(matriz)
  columnas = len(matriz[0])
  # Verifica que la matriz sea cuadrada
  if filas != columnas:
    return "La matriz ingresada no es cuadrada"
  # Aplica el método de Gauss para reducir la matriz a una triangular superior
  for i in range(filas):
    # Busca el pivote en la columna i
    pivote = matriz[i][i]
    # Si el pivote es cero, busca otra fila que tenga un valor distinto de cero
    if pivote == 0:
      for j in range(i+1, filas):
        if matriz[j][i] != 0:
          # Intercambia las filas i y j
          matriz[i], matriz[j] = matriz[j], matriz[i]
          pivote = matriz[i][i]
          break
    # Si no se encuentra un pivote distinto de cero, el determinante es cero
    if pivote == 0:
      return 0
    # Divide la fila i por el valor del pivote
    for j in range(i+1, columnas):
      matriz[i][j] /= pivote
    # Resta la fila i multiplicada por el coeficiente adecuado a las demás filas
    for j in range(i+1, filas):
      coeficiente = matriz[j][i]
      for k in range(i, filas):
        matriz[j][k] -= coeficiente * matriz[i][k]
  # El determinante es el producto de los elementos de la diagonal principal
  producto = 1
  for i in range(filas):
    producto *= matriz[i][i]
  return producto