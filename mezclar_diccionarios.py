def mezclar_diccionarios(dic1, dic2):
    # copiamos el primer diccionario (para que no se cambie el diccionario inicial)
    dic_merged = dic1.copy()
    
    # for que recorre el segundo diccionario 
    for clave, valor in dic2.items():
        # condicion que revisa si la pareja del segundo diccionario no esta dentro del primer diccionario
        # para que asi no tome en cuenta esos valores del segundo repetidos en cambiar al primero
        if clave not in dic_merged:
            # en caso de que no este, se le asigna esa pareja del segundo en el primer diccionario
            dic_merged[clave] = valor
    return dic_merged
if __name__=="__main__":
    # diccionarios que se quiera comparar (pueden usarse los que se necesiten o 
    # hacerse con las entradas del usuario como se hizo en el punto anterior)
    dic1:dict={}
    dic2:dict={}
    # llamado de la funcion
    print(str(mezclar_diccionarios(dic1, dic2)))