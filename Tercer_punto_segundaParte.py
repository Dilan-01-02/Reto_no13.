'''
Dado el JSON:
{
	"jadiazcoronado":{
		"nombres": "Juan Antonio",
		"apellidos": "Diaz Coronado",
		"edad":19,
		"colombiano":true,
		"deportes":["Futbol","Ajedrez","Gimnasia"]
	},
	"dmlunasol":{
		"nombres": "Dorotea Maritza",
		"apellidos": "Luna Sol",
		"edad":25,
		"colombiano":false,
		"deportes":["Baloncesto","Ajedrez","Gimnasia"]
	}
}
Cree un programa que lea de un archivo con dicho JSON y:

- Imprima los nombres completos (nombre y apellidos) de las personas que est�en en un rango de edades dado por el usuario.

'''
import json # Immportacion de Json
from Tercer_punto_primeraParte import leerJson # Importacion de la funcion leerJson desde Tercer_punto_primeraParte

def nombreEdad(data:dict,edadMenor:int,edadMayor:int):
    """Función que imprime el nombre de una persona que este en un rango de edad 

    Args:
        data (dict): Primer parámetro.
            Diccionario que contiene el json.
        edadMenor (dict): Segundo parámetro.
            Edad mínima en el rango solicitado.
        edadMayor (dict): Tercer parámetro.
            Edad máxima en el rango solicitado.

    Returns:
        list: dict
    """
    for i in data.values(): # Ciclo for que obtiene el rango de edad escrito e imprime el nombre de las personas que se encuentren en dicho rango 
        if edadMenor <= i["edad"] and edadMayor >= i["edad"]:
            print("Nombre de la persona en ese rango de edad: {} {}".format(i["nombres"],i["apellidos"]))

if __name__ == "__main__":
    archivo = r'C:\Users\Dilan Torres Muñoz\OneDrive\Documentos\Dilan Torres\Universidad Nacional de Colombia\Ingenieria Electrica\Semestre 1\Programación de computadores\Retos\Reto 13\Archivo.json'
    data = leerJson(archivo)
    edadMenor = int(input("Ingrese la edad menor: "))
    edadMayor = int(input("Ingrese la edad mayor: "))
    nombreEdad(data,edadMenor,edadMayor)