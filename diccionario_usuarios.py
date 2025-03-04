

import json
if __name__=="__main__":

    json_string = '''
    {
        "jadiazcoronado": {
            "nombres": "Juan Antonio",
            "apellidos": "Diaz Coronado",
            "edad": 19,
            "colombiano": true,
            "deportes": ["Futbol", "Ajedrez", "Gimnasia"]
        },
        "dmlunasol": {
            "nombres": "Dorotea Maritza",
            "apellidos": "Luna Sol",
            "edad": 25,
            "colombiano": false,
            "deportes": ["Baloncesto", "Ajedrez", "Gimnasia"]
        }
    }
    '''

    # deserialización del json siendo este en formato string
    json_usable:dict= json.loads(json_string)

    # muestra del diccionario generado en python (para pruebas)
    print(json_usable)

    # revision del deporte que quiera elegir el usuario
    # se usa la entrada con .lower(), para que no haya confuciones con los deprotes
    deporte_elegido = input("Ingrese el deporte para buscar (sin tildes, ni acentos): ").lower()  
    # preaparcion para la siguiente informacion
    print("Personas que practican " + deporte_elegido)

    # for que recorre los items del diccionario de la deserializacion
    for usuario, tipo_dato in json_usable.items():
        # esta es la parte compleja de comprobar
        # condicional que revisa que el deporte elegido este en alguno de los deportes del usuario
        # esto lo hace haciendo una variable contabmplada con .lower() para evitar confusiones de tipos
        # que esta asignada con los valores de cada uno de los deportes del diccionario deportes
        # (tipo de dato["deportes"]), recorreidnolo con unfor
        if deporte_elegido in [deporte.lower() for deporte in tipo_dato["deportes"]]:
            #muestra el usuario que "practica ese deporte"
            print(tipo_dato['nombres'] + " " + tipo_dato['apellidos'])

    # entrada de infromacion sobre el rango elegido
    edad_min = int(input("Ingrese la edad minima: "))
    edad_max = int(input("Ingrese la edad maxima: "))
    #muestra de los rangos
    print("Personas con edades entre " + str(edad_min) + " y " + str(edad_max) + ":")

    for usuario, tipo_dato in json_usable.items():
        # condicional que revisa si la edad del diccionario esta dentro del rango porporcionado
        if edad_min <= tipo_dato["edad"] <= edad_max:
            # muestra de infromacion
            print(tipo_dato['nombres'] + " " + tipo_dato['apellidos'])
