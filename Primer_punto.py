'''
Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.
'''
def crearDiccionario(x:int,numero:str) -> dict:
    """Función que crea y llena un diccionario vacio de un tamaño x recibido como parámetro 

    Args:
        x (int): Primer parámetro.
            Número de elementos del dicconario.
        numero (str): Segundo parámetro.
            Identificador del diccionario.

    Returns:
        list: dict
    """
    dict = {}
    print("\nDICCIONARIO "+str(numero))
    for i in range(x): # Ciclo for que realiza el llenado del diccionario vacio 
        clave = str(input("Ingrese la clave {}: ".format(i+1)))
        dict[clave] = str(input("Ingrese el valor {}: ".format(i+1)))
        dict.update(dict)
    
    return dict

def ordenarDiccionarioPorValor(diccionario:dict):
    """Función ordena el diccionario de forma ascendente por su valor  

    Args:
        diccionario (dict): Primer parámetro.
            Diccionario que se ordenará

    """
    dic = sorted(diccionario.items(), key = lambda  i: i[1]) # Uso del metodo sorted el cual utiliza una función anonima (la cual envia los valores del diccionario) como la clave de ordenamiento 
    print("Diccionario ordenado de forma ascendente: {}".format(dict(dic)))

if __name__ == "__main__":
    x = int(input("Ingrese la cantidad de elementos que tendrá el diccionario: "))
    diccionario = crearDiccionario(x,"")
    print("\nDiccionario original: {}".format(diccionario))
    ordenarDiccionarioPorValor(diccionario)