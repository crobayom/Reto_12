import requests

# definimos las url de las apis a las que nos vamos a conectar
api_urls = [
    "https://api.agify.io?name=michael",  # api para predecir la edad basada en un nombre
    "https://api.genderize.io?name=michael",  # api para predecir el género basado en un nombre
    "https://api.randomuser.me/"  # api para generar un usuario aleatorio
]

# función para conectarse a las apis y procesar los datos
def obtener_datos_api(api_url):
    try:
        # realizamos la solicitud get a la api
        response = requests.get(api_url)
        
        # comprobamos si la solicitud fue exitosa (código 200)
        if response.status_code == 200:
            # obtenemos el json de la respuesta
            datos_json = response.json()
            print("\ndatos de la api: " + str(api_url))
            # imprimimos el json completo
            print(datos_json)
            print("\npares de llave: valor:")

            # recorremos los pares de llave: valor y los imprimimos
            for key, value in datos_json.items():
                print(str(key) + ": " + str(value))
        else:
            print("error al conectarse a la api: " + str(api_url) + " con código de estado " + str(response.status_code))
    
    except Exception as e:
        print("se produjo un error al intentar conectarse a la api: " + str(api_url) + ". error: " + str(e))

# conectarse y procesar cada api en la lista
for url in api_urls:
    obtener_datos_api(url)
