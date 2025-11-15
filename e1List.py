nombres = ["Julian", "Carlos", "Marlos", "Ronaldo", "Mateo"]

print(nombres)
nuevo_nombre = input("Ingrese un nombre para agregar a la lista:")

# Con esta condicional verificamos que no se repitan nombres en la lista
# Usamos el metodo .append para añadir un nuevo elemento a la lista para luego imprimirlo
if nuevo_nombre in nombres:
   print("Este nombre ya esta en la lista")
else:
    nombres.append(nuevo_nombre)
    print("Nombre agregado correctamente")

# con la función print podemos imprimir el contenido de la lista
print(nombres)

# Le pedimos al usuario un valor y lo almacenamos en una variable
cambiar_nombre = input("Ingrese el nombre que quiere añadir:")
indice = int(input("Ingrese el indice del nombre que quiere cambiar:"))

# Creamos una condicional para verificar que el nombre no exista 
# Creamos un conjunto de valores posibles para mostrar los resultado del usuario

if cambiar_nombre in nombres:
    print("Este nombre ya existe en la lista:")
else:
   if indice == 0:
      nombres[indice] = cambiar_nombre
      print(nombres)
   elif indice == 1:
      nombres[indice] = cambiar_nombre
      print(nombres)
   elif indice == 2:
      nombres[indice] = cambiar_nombre
      print(nombres)    
   elif indice == 3:
      nombres[indice] = cambiar_nombre
      print(nombres)
   elif indice == 4:
      nombres[indice] = cambiar_nombre
      print(nombres)
   elif indice == 5:
      nombres[indice] = cambiar_nombre
      print(nombres)
   else:
      print("Ingrese un numero o nombre valido")

# Le pedimos al usuario el indice del elemento que quiere eliminar
eliminar_indice = int(input("Ingrese el indice del nombre que quieres eliminar (0 - 5)"))

# Creamos un conjunto de posibles valores para mostrar el resultado
# Usamos el metodo .pop para eliminar elemntos de una lista segun su indice
if eliminar_indice == 0:
    nombres.pop(eliminar_indice)
    print(nombres)
elif eliminar_indice == 1:
    nombres.pop(eliminar_indice)
    print(nombres)
elif eliminar_indice == 2:
    nombres.pop(eliminar_indice)
    print(nombres)    
elif eliminar_indice == 3:
    nombres.pop(eliminar_indice)
    print(nombres)
elif eliminar_indice == 4:
    nombres.pop(eliminar_indice)
    print(nombres)
elif eliminar_indice == 5:
    nombres.pop(eliminar_indice)
    print(nombres)