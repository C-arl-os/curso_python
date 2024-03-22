def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

frase_resultante = frase(adjetivo="capo",nombre="carlos",apellido="sancir")
print(frase_resultante)