#creando una función simple
def saludar():
    print("hola como andas")
   
#ejecutando la función simple 
saludar()

#una funcion que tenga parametro
def saludar2(nombre,sexo):
    sexo = sexo.lower()
    if(sexo == "mujer"):
        adjetivo = "mujer"
    elif (sexo=="hombre"):
        adjetivo="hombre"
    else:
        adjetivo = "amor"
    
    print(f"Hola como andas {nombre}, mi {adjetivo}")

saludar2("carlos","")

#crear una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num-2
    c2 = num
    c3 = num-5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return (contraseña,num)
    
#desempaquetando la funcion
password ,primer_numero= crear_contraseña_random(398)

#mostrando los resultados
frase = f"tu contraseña nueva es: {password} y el numero es {primer_numero}"
print(frase)