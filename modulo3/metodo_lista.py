#creando una lista con list
lista = list(["Hola","Carlos",20])
lista2= list([32,2,20,6,0])

#cantidad de elementos
print(len(lista))

#agregando elemnos a la lista
agregando = lista.append("sancir")
print(lista)

#agregamos un elemento en un indice especifico
lista.insert(2,"Emanuel")
print(lista)

#agregar varios elementos a la lista
lista.extend([False,2030])
print(lista)

#eliminar un elemento de la lista(por su indice)
lista.pop(-1)
print(lista)

#removiendo un elemento de la lista por su valor
lista.remove("Emanuel")
print(lista)

#ordena elementos de forma ascendente  so
lista2.sort()
print(lista2)

#invirtiendo elementos
lista2.reverse()
print(lista2)

#buscar la posción
print(lista.index(20))

#elimininando todos los elemento de la lista
lista.clear()
print(lista)