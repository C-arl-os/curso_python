#creando una funcion que nos devuelva los numero primos
#entre 0 y el argumento que pasamos

#crear una funcion que verifique si un numero es primo
def es_primo(num):
    #verufucando que el numero no pueda dividirse 
    #por ningun numero entre 2 y ese mismo numero -1
    for i in range(2,num):
        #si es divisible por alguno retorna false y termina el bucle
        if num%i ==0: 
            return False
    #si termina el bucle, significa que no fue divisible entonces es primo
    return True

#creando funcion que retorna una lista con todos los primos
def primo_hasta(num):
    #creamos la lista
    primos = []
    for i in range(3,num+1):
        #verificamos si el valor es primo
        resultado = es_primo(i)
        #en caso de que sea lo agregamos a la lista
        if resultado == True: primos.append(i)
        
    return primos

resultado = primo_hasta(13)
print(resultado)
        
            