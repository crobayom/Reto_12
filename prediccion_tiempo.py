from datetime import datetime, timezone  # importamos las clases necesarias para manejar fechas
import json  # importamos la librería json para trabajar con datos en formato json

# función para convertir el número que representa un momento específico en el tiempo
# a un objeto datetime
def obtener_fecha_real(utc_timestamp: int) -> datetime:
    # convierte el número que representa un momento específico en el tiempo 
    # (en segundos desde el 1 de enero de 1970, por ejemplo)
    # a un objeto datetime en zona horaria UTC
    # usa la zona horaria UTC para garantizar la conversión correcta
    return datetime.fromtimestamp(utc_timestamp, timezone.utc)  

# función principal que procesa los datos del diccionario con las alertas
def procesar_alertas(diccionario):
    # recorremos todas las alertas del diccionario, suponiendo que solo se tendrán datos para 8 días
    for i in range(len(diccionario['alert_precip'])):
        # mostramos para depuración el índice y los valores del diccionario
        print(f"\nProcesando día {i + 1}...")

        # Mostramos las alertas de cada tipo para depurar
        print("alert_precip:", diccionario['alert_precip'][str(i)])
        print("alert_vel_viento:", diccionario['alert_vel_viento'][str(i)])
        print("alert_tmp_max:", diccionario['alert_tmp_max'][str(i)])
        print("alert_tmp_min:", diccionario['alert_tmp_min'][str(i)])
        print("alert_alertas:", diccionario['alert_alertas'][str(i)])

        # revisamos si existe una alerta de precipitación para el día actual
        if diccionario['alert_precip'][str(i)] != "-":
            # si hay alerta, obtenemos el número que representa el momento específico en el tiempo para ese día
            fecha_utc = diccionario['dt'][str(i)]
            # convertimos ese número a un objeto datetime con la función que creamos antes
            fecha_real = obtener_fecha_real(fecha_utc)  # convertimos el número a fecha real
            # imprimimos la alerta de precipitación
            print("alerta de precipitación:")
            # mostramos la fecha de manera legible
            print("fecha:", str(fecha_real))  
            # mostramos el nivel de precipitación
            print("nivel de precipitación:", str(diccionario['prcp'][str(i)]))  
            # dejamos una línea en blanco para facilitar la lectura
            print()  
        else:
            print("No hay alerta de precipitación para el día", i + 1)

        # revisamos si hay alerta de vientos
        if diccionario['alert_vel_viento'][str(i)] != "-":
            fecha_utc = diccionario['dt'][str(i)]
            fecha_real = obtener_fecha_real(fecha_utc)
            print("alerta de vientos:")
            print("fecha:", str(fecha_real))
            # mostramos la velocidad del viento
            print("velocidad del viento:", str(diccionario['vel_viento'][str(i)]))  
            print()
        else:
            print("No hay alerta de vientos para el día", i + 1)
        
        # revisamos si hay alerta de temperatura máxima
        if diccionario['alert_tmp_max'][str(i)] != "-":
            fecha_utc = diccionario['dt'][str(i)]
            fecha_real = obtener_fecha_real(fecha_utc)
            print("alerta de temperatura máxima:")
            print("fecha:", str(fecha_real))
            # mostramos la temperatura máxima
            print("temperatura máxima:", str(diccionario['tmp_max'][str(i)]))  
            print()
        else:
            print("No hay alerta de temperatura máxima para el día", i + 1)
        
        # revisamos si hay alerta de temperatura mínima
        if diccionario['alert_tmp_min'][str(i)] != "-":
            fecha_utc = diccionario['dt'][str(i)]
            fecha_real = obtener_fecha_real(fecha_utc)
            print("alerta de temperatura mínima:")
            print("fecha:", str(fecha_real))
            # mostramos la temperatura mínima
            print("temperatura mínima:", str(diccionario['tmp_min'][str(i)]))  
            print()
        else:
            print("No hay alerta de temperatura mínima para el día", i + 1)

        # revisamos si hay alguna alerta general
        if diccionario['alert_alertas'][str(i)] != "-":
            fecha_utc = diccionario['dt'][str(i)]
            fecha_real = obtener_fecha_real(fecha_utc)
            print("alerta general:")
            print("fecha:", str(fecha_real))
            # mostramos la descripción de la alerta general
            print("descripción:", str(diccionario['alert_alertas'][str(i)]))  
            print()
        else:
            print("No hay alerta general para el día", i + 1)

# aquí cargamos el json de ejemplo que contiene los datos del pronóstico
json_string = '''{
    "dt": {"0": 1685116800, "1": 1685203200, "2": 1685289600, "3": 1685376000, "4": 1685462400, "5": 1685548800, "6": 1685635200, "7": 1685721600},
    "alert_precip": {"0": "X", "1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-"},
    "alert_vel_viento": {"0": "-", "1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-"},
    "alert_tmp_max": {"0": "-", "1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-"},
    "alert_tmp_min": {"0": "-", "1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-"},
    "alert_alertas": {"0": "-", "1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-"},
    "prcp": {"0": 40.0, "1": 1.65, "2": 14.01, "3": 5.07, "4": 16.55, "5": 2.17, "6": 2.77, "7": 1.73},
    "vel_viento": {"0": 3.56, "1": 5.07, "2": 5.38, "3": 3.95, "4": 4.74, "5": 3.75, "6": 4.08, "7": 5.94},
    "tmp_max": {"0": 27.16, "1": 31.1, "2": 30.2, "3": 29.5, "4": 28.87, "5": 29.78, "6": 28.96, "7": 28.25},
    "tmp_min": {"0": 25.64, "1": 24.64, "2": 25.84, "3": 25.56, "4": 25.72, "5": 24.86, "6": 25.96, "7": 25.47}
}'''

# cargamos el diccionario desde el json
diccionario = json.loads(json_string)

# ejecutamos la función que procesa las alertas solo si este es el archivo principal
if __name__ == "__main__":
    # llamamos a la función para procesar las alertas y mostrar la información
    procesar_alertas(diccionario)
