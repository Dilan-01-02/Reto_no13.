'''
A través de un programa conectese a al menos 3 API's , obtenga el JSON, imprimalo y extraiga los pares de llave : valor.

'''
import json # Importación del Json 
import requests # Importación del Requests
from pprint import pprint # Importacion del pprint

url1 = requests.get('https://www.boredapi.com/api/activity') # Primera api
url2 = requests.get('https://official-joke-api.appspot.com/random_joke') # Segunda api
url3 = requests.get('https://api.zippopotam.us/us/33162') # Tercera api

def imprimirJson(url,num:int):
    """Función que imprime un json de una api

    Args:
        url : Primer parámetro.
            Enlace de la API.
        num (int): Segundo parámetro.
            identificador de JSON.
    """
    data = url.json()
    print("\nJSON API "+str(num))
    pprint(data)

def imprimirPares(url,num:int):
    """Función que imprime los pares clave - valor del json de una api

    Args:
        url : Primer parámetro.
            Enlace de la API.
        num (int): Segundo parámetro.
            identificador de JSON.
    """
    data = url.json()
    print("\nPARES ClAVE : VALOR DEL JSON "+str(num))
    for i in data: # Ciclo for que imprime la clave valor del jason
        print("{} - {}".format(i,data[i]))

if __name__ == "__main__":
    imprimirJson(url1,1)
    imprimirJson(url2,2)
    imprimirJson(url3,3)
    print("\n============================")
    imprimirPares(url1,1)
    imprimirPares(url2,2)
    imprimirPares(url3,3)