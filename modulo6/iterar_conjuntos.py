
animales = {"gato","perro","loro","cocodrilo"}
numeros = {10,62,12,72}

#recorriendo la lista animales
for animal in animales:
  print("Ahora la varibale animal es igual a: "+animal)
 
 #recorriendo la lista numero y multiplicando por 10 
for numero in numeros:
    print(numero*10)
    
#iterando 2 lista al mismo tiempo
for  numero,animal in zip(animales,numeros):
    print("recorriendo lista 1: "+numero)
    print("recorriendo lista 2: ",animal)
    
for num in range(5,10):
    print(num)
    
for num in enumerate(numeros):
   indice = num[0]
   valor = num[1]
   print(f"el indice es: {indice} y el valor es: {valor}")
   
#usando el else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")    