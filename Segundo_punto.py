'''
Desarrollar una función que reciba dos diccionarios como parámetros y los mezcle, es decir, que se construya un 
nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar 
el valor que tenga la clave en el primer diccionario.
'''
from Primer_punto import crearDiccionario

def mezclarDiccionarios(dicc1:dict,dicc2:dict):
    """Función que mezcla dos diccionarios y asigna el valor del primer diccionario en caso de tener claves repetidas

    Args:
        dicc1 (dict): Primer parámetro.
            Primer diccionario que se mezclara.
        dicc2 (str): Segundo parámetro.
            ISegundo diccionario que se mezclara.

    """
    mezcla = list(dicc2.items()) + list(dicc1.items()) # Obtención de los items de cada diccionario y sumado de las listas resultantes para de nuevo convertirlo a diccionario
    mezcla = dict(sorted(mezcla))
    print("\nDiccionarios mezclados: {}".format(mezcla))

if __name__ == "__main__":
    x = int(input("Ingrese la cantidad de elementos que tendrá el primer diccionario: "))
    y = int(input("Ingrese la cantidad de elementos que tendrá el segundo diccionario: "))
    dicc1 = crearDiccionario(x,1)
    dicc2 = crearDiccionario(y,2)
    print("\nDiccionario 1: {}".format(dicc1))
    print("Diccionario 2: {}".format(dicc2))
    mezclarDiccionarios(dicc1,dicc2)