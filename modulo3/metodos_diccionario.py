diccionario = {
    "nombre" : 'carlos',
    "apellido" : "sancir",
    "sub" : '100'
}
#nos devuelve un objeto dict.item
claves = diccionario.keys()
print(claves)

#obteniendo un elemento 
claves = diccionario.get("sub")
print(claves)

#obteniendo un elemento disct_item
diccionario_iterable = diccionario.items()
print(diccionario_iterable)


#eliminando un elemento del diccionario
diccionario.pop("nombre")
print(diccionario)
#eliminando todo del diccionario
diccionario.clear()
print(diccionario)