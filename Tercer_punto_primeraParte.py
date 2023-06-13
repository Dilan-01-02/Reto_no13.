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

- Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.

'''
import json  # Importacion del Json

def leerJson(archivo):
    """Función que lee el archivo tipo json

    Args:
        archivo (int): Primer parámetro.
            Archivo json que se leerá.

    Returns:
        list: data
    """
    with open(archivo) as file:
        data = json.load(file)
    return data

def nombreDeportes(data:dict,deporte:str):
    """Función que imprime los nombres de las personas que practiquen un deporte

    Args:
        data (dict): Primer parámetro.
            Diccionario que contiene el json.
        deporte (dict): Segundo parámetro.
            Deporte con el cual se identificará a la persona.

    """
    for i in data.values(): # Ciclo for que obtiene el deporte escrito y devuelve el nombre de la persona que lo practica
        if deporte in i["deportes"]:
            print("Nombre de la persona que practica el deporte: {} {}".format(i["nombres"],i["apellidos"]))

if __name__ == "__main__":
    archivo = r'C:\Users\Dilan Torres Muñoz\OneDrive\Documentos\Dilan Torres\Universidad Nacional de Colombia\Ingenieria Electrica\Semestre 1\Programación de computadores\Retos\Reto 13\Archivo.json'
    data = leerJson(archivo)
    deporte = str(input("Ingrese el deporte: ")) 
    nombreDeportes(data,deporte)