numeros = [4,7,1,42,15]

#enocntrar el numero mayor en una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#enocntrar el numero menor en una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#redondear a 6 decimales
numero = round(12.345678,6)
print(numero)

#retorna false ->0, vacio false, ninguno
resultado = bool(0)
print(resultado)

#retorna true, si todos los valores son verdaderos
resultado = all([0,"true",[23,32]])
print(resultado)

#suma todos los valores de un iterable
suma = sum(numeros)
print(suma)