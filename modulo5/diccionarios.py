#creando diccionarios con dict()
diccionario = dict(nombre="carlos", apellido="sancir")

#las listas no pueden ser claves
diccionario = {frozenset(["dalto","rancio"]):"jaja"}

#creando diccionarios con fromkwys()
diccionario = dict.fromkeys(["nombre","ellido"])
print(diccionario)