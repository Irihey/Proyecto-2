#Funcion valInt


def valInt(numero, arreglo = None): 
    variable = True # Se inicia una variable booleana llamada variable con el valor de True
    if not isinstance(numero, int): #isintance es una funcion de verificacion, este caso para saber si el numero es un entero
        variable = False
        return variable
    if arreglo != None: # se verifica si el argumento arreglo no es None
        if isinstance(arreglo, tuple):
            if arreglo[0] >= arreglo[-1]:
                raise ValueError
            elif len(arreglo) != 2:
                raise ValueError
            elif numero <= arreglo[0] or numero >=arreglo[-1]:
                variable = False
        elif isinstance(arreglo, list):
            if arreglo[0] >= arreglo[-1]:
                raise ValueError
            elif len(arreglo) != 2:
                raise ValueError
            elif numero < arreglo[0] or numero > arreglo[-1]:#se verifica si el modulo del numero entero esta fuera del rango especificado por los elementos de la lista, si esta afuera arroja False
                variable = False
        else:
            raise TypeError
    return variable 



#Función valFloat

def valFloat(numero, arreglo = None):
    variable = True
    if not isinstance(numero, float):
        variable = False
    if arreglo != None:
        if isinstance(arreglo, tuple):
            if arreglo[0] >= arreglo[-1]:
                raise ValueError
            elif len(arreglo) != 2:
                raise ValueError            
            elif numero <=arreglo[0] or numero >=arreglo[-1]:
                variable = False 
        elif isinstance(arreglo,list):
            if arreglo[0] >= arreglo[-1]:
                raise ValueError
            elif len(arreglo) != 2:
                raise ValueError
            elif numero < arreglo[0] or numero > arreglo[-1]:
                variable = False
        else:
            raise TypeError
    return variable



#Función valComplex

def valComplex(numero, arreglo = None):
    variable = True # Se inicia una variable booleana llamada variable con el valor de True
    if not isinstance(numero, complex):# Se verifica si el argumento no es un numero complejo
        variable = False
    if arreglo != None: # se verifica si el argumento arreglo no es None
        complex_num_module = abs(numero)# se calcula el modulo del numero complejo, utulizando la funcion abs() y se guarda en la variable complex_num_module
        if isinstance(arreglo, tuple): #Se verifica si el arreglo es una tuple
            if arreglo[0] >= arreglo[-1]: #veridicar si el primer elemento es mayor o igual al ultimo
                raise ValueError
            elif len(arreglo) != 2: #se verifica que la longitud de la tupla no es igual a 2, se arroja un error
                raise ValueError
            elif complex_num_module <= arreglo[0] or complex_num_module >= arreglo[-1]: #se verifica si el modulo del numero complejo esta fuera del rango especificado por los elementos de la lista, si esta fue arroja False
                variable = False
        elif isinstance(arreglo, list):
            if arreglo[0] >= arreglo[-1]:
                raise ValueError
            elif len(arreglo) != 2:
                raise ValueError
            elif complex_num_module < arreglo[0] or complex_num_module > arreglo[-1]:
                variable = False
        else:
            raise TypeError
    return variable



#Función valList

def valList(variable_1, variable_2=None, variable_3=None):
    if variable_2 is None and variable_3 is None:
        if isinstance(variable_1, list):
            return True
        else:
            return False
    elif variable_2 is not None and variable_3 is not None:       
        if  (isinstance(variable_2, list) or isinstance(variable_2, int)) and isinstance(variable_3, str):
            if variable_3 == 'values':
                if isinstance(variable_1, list) and variable_1 == variable_2:
                    return True
                else:
                    return False  
            elif variable_3 == 'len':
                if isinstance(variable_1, list) and isinstance(variable_2, int) and isinstance(variable_3, str) and len(variable_1) == variable_2:
                    return True
                else:
                    return False
            else:
                raise ValueError("El tercer valor debe ser 'values' o 'len'")
        else:
            raise TypeError("El tipo de argumento 2 debe ser list o int y el tipo del argumento 3 debe ser str")
    elif isinstance(variable_2, int) and isinstance(variable_3, str):
        return True
    else:
        raise TypeError("La funcion valList() debe recibir 1 o 3 valores")