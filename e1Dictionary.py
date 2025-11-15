inventario = {
    "Azucar": 1500,
    "Sal": 800,
    "Arroz": 3200,
    "Aguacate": 4800
}

# Usamos la función print para mostrar el inventario
print(f"{inventario}\n")

# Pedimos al usario la clave (Producto) y su contenido (Precio)
producto = str(input("¿Que producto deseas agregar al inventario?:"))
precio = int(input("Ingrese el precio del producto:"))

# Agregamos el producto y su respectivo precio al inventario
inventario[producto] = precio
print(f"{inventario}\n")

# Pedimos al usuario el nombre del producto, en este caso seria la clave 
producto_consultado = str(input("Ingrese el nombre del producto para consultar su precio:"))

# Consultamos el precio del producto
consultar_precio = inventario[producto_consultado]
print(f"El precio del producto {producto_consultado} es de: {consultar_precio}")

# Pedimos al usuario los datos del producto a modificar
modificar_producto = str(input("Ingrese el producto que quiere modificar:"))
precio_nuevo = int(input("Ingrese el nuevo precio del producto:"))

# Modificamos el contenido del producto mediante su clave
inventario[modificar_producto] = precio_nuevo
print("Precio modificado con exito")
print(inventario)

# Pedimos al usuario el nombre del producto, osea la clave
producto_eliminado = str(input("Ingrese el nombre del producto a eliminar:"))

# Eliminados con un "del" la clave y el contenido del producto
del inventario[producto_eliminado]
print(inventario)