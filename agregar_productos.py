def agregar_producto(productos_almacen):
    # Solicitar datos al usuario
    nombre_producto = input("Introduce el nombre del producto: ")
    cantidad = int(input("Introduce la cantidad del producto: "))
    precio = float(input("Introduce el precio del producto: "))
    estanteria = input("Introduce la estantería donde se ubicará el producto: ")

    # Crear el nuevo producto como un diccionario
    nuevo_producto = {"nombre": nombre_producto, "cantidad": cantidad, "precio": precio}

    # Verificar si la estantería ya existe en el almacén
    if estanteria in productos_almacen:
        # Agregar el nuevo producto a la lista de productos de la estantería
        productos_almacen[estanteria].append(nuevo_producto)
    else:
        # Crear una nueva estantería con el nuevo producto
        productos_almacen[estanteria] = [nuevo_producto]

    # Mensaje de confirmación
    print(f"Producto '{nombre_producto}' agregado correctamente a la estantería '{estanteria}'.")

# Ejemplo de uso:
productos_almacen = {
    "Estantería A": [{"nombre": "Chocolate Amargo", "cantidad": 20, "precio": 2.5}, {"nombre": "Mermelada de Fresa", "cantidad": 15, "precio": 3.0}], 
    "Estantería B": [{"nombre": "Aceitunas Verdes", "cantidad": 50, "precio": 1.5}, {"nombre": "Aceite de Oliva Extra", "cantidad": 10, "precio": 6.0}], 
    "Estantería C": [{"nombre": "Café Molido", "cantidad": 25, "precio": 5.0}, {"nombre": "Té Verde", "cantidad": 40, "precio": 2.0}],
    "Estantería D": [{"nombre": "Pasta Integral", "cantidad": 30, "precio": 1.8}, {"nombre": "Arroz Basmati", "cantidad": 20, "precio": 1.7}]
}

agregar_producto(productos_almacen)
print(productos_almacen)
