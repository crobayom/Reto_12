

def entradas(diccionario:dict, tipo_llave, tipo_valor)->None:
    # busqueda del tipo (siendo el identificador del tipo un int) con algo del tipo "switch-case" pero pythonico
    # con cada lugar que se quiera revisar siendo traducida la entrada al tipo de dato requerido 
    #para las llaves
    if tipo_llave==1:
        llave:int=int(input("Ingrese el entero que quiera ingresar como llave: "))
    elif tipo_llave==2:
        llave:float=float(input("Ingrese el flotante que quiera ingresar como llave: "))
    elif tipo_llave==3:
        llave:str=str(input("Ingrese el string que quiera ingresar como llave: "))
    elif tipo_llave==4:
        llave:tuple=tuple(input("Ingrese la tupla que quiera ingresar como llave (siendo cada caracter un valor separado): "))
        print(llave)
    
    #lomismo que arriba pero ahora para los valores
    if tipo_valor == 1: 
        valor = int(input("Ingrese el valor entero: "))
    elif tipo_valor == 2:
        valor = float(input("Ingrese el valor flotante: "))
    elif tipo_valor == 3:
        valor = str(input("Ingrese el valor string: "))
    elif tipo_valor == 4:
        valor = tuple(input("Ingrese el valor como tupla (separado por comas): "))


    # actualiza el diccionario con la pareja ahora ingresada
    diccionario[llave] = valor

def impresion_ascendente (diccionario:dict)-> None:
    # obtiene ordenado el diccionario por sus valores
    diccionario_sorteado=sorted(diccionario.values())
    # for que recorrera las parejas del diccionario ordenado por sus valores
    for diccionario in diccionario_sorteado:
        # imprime cada pareja del diccionario hasta que acabe (estando estas ya en orden)
        print(diccionario)


if __name__=="__main__":
    
    # inicializacion del diccinario en vacio para evitar problemas (gracias diccionarios por dejarse mutar)
    diccionario:dict={}
    # entrada de informacion sobre la cantidad de parejas a poner en el diccionario
    cantidad_de_llaves:int=int(input("Ingrese la cantidad de parejas que quiera ingresar: "))
    # inicio de una variable con un valor que no entra en el rango permitido para asegura la ocurrencia de la comprobacion
    tipo_llave:int=0
    #comprobacion del valor ingresado por el usuario (que este dentro de los rangos)
    while tipo_llave<1 or tipo_llave>5:
        tipo_llave=int(input("Ingrese el tipo de dato que quiere para poner de llave. 1. int 2. float 3. str 4. tuple : "))
        if tipo_llave<1 or tipo_llave>5: print("El tipo elegido no existe, intentelo de nuevo")
    
    # lo mismo que arriba pero con otra variable
    tipo_valor:int=0
    while tipo_valor<1 or tipo_valor>5:
        tipo_valor=int(input("Ingrese el tipo de dato que quiere para poner de valor. 1. int 2. float 3. str 4. tuple : "))
        if tipo_valor<1 or tipo_valor>5: print("El tipo elegido no existe, intentelo de nuevo")
    
    # llamado de la funcion que agrega los valores a un diccionario repetida cuantas veces el usuario haya decidio agregarlas
    for i in range(cantidad_de_llaves):
        entradas(diccionario, tipo_llave, tipo_valor)

    # impresion ascendete de informacion
    impresion_ascendente(diccionario)

