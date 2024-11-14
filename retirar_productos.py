def mostrar_productos_disponibles(productos_almacen):
    print("Productos disponibles en el almacén:")
    for estanteria, productos in productos_almacen.items():
        print(f"\n{estanteria}:")
        for producto in productos:
            print(f" - {producto['nombre']}: {producto['cantidad']} unidades, {producto['precio']} euros/unidad")

def retirar_producto(productos_almacen):
    # Mostrar productos disponibles
    mostrar_productos_disponibles(productos_almacen)
    
    # Solicitar datos al usuario
    nombre_producto = input("Introduce el nombre del producto a retirar: ")
    cantidad_retirar = int(input("Introduce la cantidad a retirar: "))

    # Buscar el producto en las estanterías
    producto_encontrado = False
    for estanteria, productos in productos_almacen.items():
        for producto in productos:
            if producto["nombre"] == nombre_producto:
                producto_encontrado = True
                if producto["cantidad"] >= cantidad_retirar:
                    producto["cantidad"] -= cantidad_retirar
                    print(f"Se han retirado {cantidad_retirar} unidades de '{nombre_producto}' de la estantería '{estanteria}'.")
                    # Eliminar el producto si la cantidad es cero
                    if producto["cantidad"] == 0:
                        productos.remove(producto)
                    return
                else:
                    print(f"Error: No hay suficiente cantidad de '{nombre_producto}' en la estantería '{estanteria}'.")
                    return

    if not producto_encontrado:
        print(f"Error: Producto '{nombre_producto}' no encontrado en el almacén.")

# Ejemplo de uso:
productos_almacen = {
    "Estantería A": [{"nombre": "Chocolate Amargo", "cantidad": 20, "precio": 2.5}, {"nombre": "Mermelada de Fresa", "cantidad": 15, "precio": 3.0}], 
    "Estantería B": [{"nombre": "Aceitunas Verdes", "cantidad": 50, "precio": 1.5}, {"nombre": "Aceite de Oliva Extra", "cantidad": 10, "precio": 6.0}], 
    "Estantería C": [{"nombre": "Café Molido", "cantidad": 25, "precio": 5.0}, {"nombre": "Té Verde", "cantidad": 40, "precio": 2.0}],
    "Estantería D": [{"nombre": "Pasta Integral", "cantidad": 30, "precio": 1.8}, {"nombre": "Arroz Basmati", "cantidad": 20, "precio": 1.7}]
}

retirar_producto(productos_almacen)
print(productos_almacen)
