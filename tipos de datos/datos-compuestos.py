#listas en python comienzan desde 0
lista = ["Carlos", "Sancir", True, 1.65]
print(lista)
lista[2] = "Reyes"
print(lista[2])

#tuplas
tupla = ("Carlos", "Sancir", True, 1.65) #nose puede modificar
print(tupla)

#creando un cojunto (set)
conjunto = {"Carlos", "Sancir", True, 1.65} #nose puede modificar nose puede acceder por el indice
print(conjunto) #no permite repetir valores

#crando un diccionario (dict)
diccionario = {
    'nombre' : "carlos sancir",
    'apellido': "reyes",
    'edad': 20,
    
}

print(diccionario["nombre"])