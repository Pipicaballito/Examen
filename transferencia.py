def transferir_producto(productos_almacen):
    # Solicitar datos al usuario
    nombre_producto = input("Introduce el nombre del producto a transferir: ")
    cantidad_transferir = int(input("Introduce la cantidad a transferir: "))
    estanteria_origen = input("Introduce la estantería de origen: ")
    estanteria_destino = input("Introduce la estantería de destino: ")

    # Verificar si la estantería de origen y destino existen
    if estanteria_origen not in productos_almacen:
        print(f"Error: La estantería de origen '{estanteria_origen}' no existe.")
        return

    if estanteria_destino not in productos_almacen:
        print(f"Error: La estantería de destino '{estanteria_destino}' no existe. Creando nueva estantería.")
        productos_almacen[estanteria_destino] = []

    # Buscar el producto en la estantería de origen
    producto_encontrado = False
    for producto in productos_almacen[estanteria_origen]:
        if producto["nombre"].lower() == nombre_producto.lower():
            producto_encontrado = True
            if producto["cantidad"] >= cantidad_transferir:
                producto["cantidad"] -= cantidad_transferir

                # Buscar si el producto ya existe en la estantería de destino
                for prod_destino in productos_almacen[estanteria_destino]:
                    if prod_destino["nombre"].lower() == nombre_producto.lower():
                        prod_destino["cantidad"] += cantidad_transferir
                        print(f"Se han transferido {cantidad_transferir} unidades de '{nombre_producto}' de '{estanteria_origen}' a '{estanteria_destino}'.")
                        if producto["cantidad"] == 0:
                            productos_almacen[estanteria_origen].remove(producto)
                        return
                
                # Si el producto no existe en la estantería de destino, añadirlo
                productos_almacen[estanteria_destino].append({"nombre": nombre_producto, "cantidad": cantidad_transferir, "precio": producto["precio"]})
                print(f"Se han transferido {cantidad_transferir} unidades de '{nombre_producto}' de '{estanteria_origen}' a '{estanteria_destino}'.")
                if producto["cantidad"] == 0:
                    productos_almacen[estanteria_origen].remove(producto)
                return
            else:
                print(f"Error: No hay suficiente cantidad de '{nombre_producto}' en la estantería '{estanteria_origen}'.")
                return

    if not producto_encontrado:
        print(f"Error: Producto '{nombre_producto}' no encontrado en la estantería '{estanteria_origen}'.")

# Ejemplo de uso:
productos_almacen = {
    "Estantería A": [{"nombre": "Chocolate Amargo", "cantidad": 20, "precio": 2.5}, {"nombre": "Mermelada de Fresa", "cantidad": 15, "precio": 3.0}], 
    "Estantería B": [{"nombre": "Aceitunas Verdes", "cantidad": 50, "precio": 1.5}, {"nombre": "Aceite de Oliva Extra", "cantidad": 10, "precio": 6.0}], 
    "Estantería C": [{"nombre": "Café Molido", "cantidad": 25, "precio": 5.0}, {"nombre": "Té Verde", "cantidad": 40, "precio": 2.0}],
    "Estantería D": [{"nombre": "Pasta Integral", "cantidad": 30, "precio": 1.8}, {"nombre": "Arroz Basmati", "cantidad": 20, "precio": 1.7}]
}

transferir_producto(productos_almacen)
print(productos_almacen)
