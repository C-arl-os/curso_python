
frutas = ["bananas","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "hola carlos"
numeros = [2,4,6,4]
#evitando que se coma una fruta
for fruta in frutas:
    if fruta =="granada":
        continue
    print(f"me voy a comer una {fruta}")
 
print("   ")
 #evitar que bucle siga ejecutandi
for fruta in frutas:
    print(f"me voy a comer una {fruta}")
    if fruta =="pera":
        break

#recorrer una cadena de texto

for letra in cadena:
    print(letra)

#for en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
print("bucle terminado")
