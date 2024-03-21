cadena1 = "hola,soy carlos"
cadena2 = "Bienvenido maquinola"

#dir atributos del objeto
#print(dir(cadena1))

#upper todo a mayúsculas
print(cadena1.upper())

#lower em minusculas
print(cadena1.lower())

#capitalize primera en mayuscula
print(cadena1.capitalize())

#find buscamos una cadena en otra cadena
busqueda_find = cadena1.find("s")
print(busqueda_find)

#index buscamos una cadena en otra cadena
print(cadena1.index("h"))

#ISNUMERIC si es numero devuelve true sino false
print(cadena1.isnumeric())

#devuelve la cantidad de veces que coincide 
contar_coincidencia = cadena1.count("a")
print(contar_coincidencia)

#contamos cuantos caracteres tiene una cadena
print(len(cadena1))

#verificamos si una cadena empieza con otra cadena dada
print(cadena1.startswith("a"))

#si termina 
print(cadena1.endswith("s"))

#reemplaza una cadena por otra

print(cadena1.replace(","," "))

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")
print(cadena_separada[0]) #crea una lista