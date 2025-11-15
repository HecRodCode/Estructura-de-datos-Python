catalogo = 10, 20, 30, 40, 50, 60, 

# Como las tuplas son inmutables, para agregar un vuevo valor se debe de crear una nueva 
# tupla nueva y agregar el contenido de la otra tupla mas lo que le quieres añadir
nuevo_catalogo = catalogo + (70,)
print(nuevo_catalogo)

# Como los elementos de las tuplas no se pueden modificar, lo que hacemos es convertir la tupla
# en una lista y esa lista la almacenamos en una variable.
catalogo_temporal = list(catalogo)

# Ahora que ya es una lista podemos modificar sus elementos.
catalogo_temporal[2] = 25

# Una vez ya modificada la lista lo que hacemos es convertila en una tupla de nuevo
# De esa manera podrias "modifcar" una tupla
nuevo_catalogo = tuple(catalogo_temporal)
print(nuevo_catalogo)

# Para "eliminar" un elemento de una tupla de nuevo debemos de convertirla en lista primero
catalogo_temporal2 = list(catalogo)

# Ahora que es una lista ya podemos modificarla, en este caso para eliminar un elemento
del catalogo_temporal2[1]

# Una vez eliminado el elemento, volvemos a convertirla en tupla
nuevo_catalogo2 = tuple(catalogo_temporal2)
print(nuevo_catalogo2)

# Usamos un bucle for y la funcion enumerate() para desempaquetar
# los valores en la tupla y que nos imprima una lista ordenada 
for indice, valor in enumerate(catalogo):
    print(f"Indice: {indice} - {valor}")


# Para sumar todos los valores de una tupla lo que hacemos es inicializar una variable 
# que nos recoja todos los valores en 0.

suma_total = 0

# Luego con ina varibale llamada "Valor" itereamos dentro de la tupla, para que cada
# valor sumando se añada a la varibale que inicializamos en 0
for valor in catalogo:
    suma_total += valor

print(suma_total)

# Creamos una variable que alamacene la expresion None, de esta manera esta variable no 
# va a contener valores de ningun tipo
mayor = None

# Para saber cual es el elemeeto numerico mayor en la tupla debemos recorrerla con un 
# bucle for.
for valor in catalogo:
    # Con esta condicional lo que hacemos es que si en una vuelta del for una de estas 
    # condiciones se cumple, actualizamos el valor de la variable "mayor"
    if mayor is None or valor > mayor:
        mayor = valor

print(f"El numero mayor de la tupla es: {mayor}")

# Para saber cual es el elemeeto numerico mayor en la tupla debemos recorrerla con un 
# bucle for.
menor = None

# Para saber cual es el elemeeto numerico menor en la tupla debemos recorrerla con un 
# bucle for.
for valor in catalogo:
    # Con esta condicional lo que hacemos es que si en una vuelta del for una de estas 
    # condiciones se cumple, actualizamos el valor de la variable "mayor"    
    if menor is None or valor < menor:
        menor = valor 

print(f"el numero menor de la tupla es: {menor}")

# Creamos un punto de partida en la tupla, y ese valor lo almacenaremos en una variable
num_mayor = catalogo[0]

# Con el bucle for recorreremos cada elemento de la tupla para compararlos
for num in catalogo:
    # Con esta condicional compararemos cada elemento de la tupla, de modo que si
    # alguno la cumple, almacenaremos ese valor en la variable de punto de partida
    if num > num_mayor:
        num_mayor = num

# Ya con el numero mayor listo, gracias a la funcion .index() podremos saber 
# la posicion de ese numero para luego imprimirlo
posicion = catalogo.index(num_mayor)

print(f"La posiicion del numero {num_mayor} es la {posicion}")