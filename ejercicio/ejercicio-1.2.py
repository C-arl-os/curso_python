#le pedimos al ussuario que nos diga una frase (o varias)
frase = input("decime algo maestro y te calculo cuanto tardarias si tuvieras que decirla: ")

#creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
cantidad_separadas = frase.split(" ")

#usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(cantidad_separadas)

#calculamos cuanto tardaria en decir las palabras y se lo decimos
print(f"Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo")
print(f"dalto lo diria en {cantidad_de_palabras*100//2 *1.3/100} segundos")

#calculamos cuanto tardaría en decir las palabras y se lo decimos
if cantidad_de_palabras > 120:
    print("para tampoco de pedi un testamento")