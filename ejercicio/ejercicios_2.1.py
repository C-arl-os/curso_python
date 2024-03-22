#falto el profe y los pibes van a armar la clase

#pedir el nombre y la edad de los compañeros que vinieron hoy a clase

#funcion para obtener al asistente y al profesor
def obneter_compañeros(cantidad_de_compañeros):
    
    #creando la lista con los compañeros
    compañeros = []
    
    #ejecutando un for para pedir informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        
        #agregando la informacion a la lista
        compañeros.append(compañero)
    
    #ordenando de menor a mayor segun edad
    compañeros.sort(key=lambda x:x[1])
    print(compañeros)
    
    #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    #paradefinir al sistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente,profesor

asistente,profesor = obneter_compañeros(5)
print(f"el profesor es: {profesor} y su asistente es {asistente}")
