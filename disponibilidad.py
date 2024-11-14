def verificar_disponibilidad(productos_almacen):
    # Solicitar nombre del producto al usuario
    nombre_producto = input("Introduce el nombre del producto a verificar: ")

    cantidad_total = 0
    estanterias = []

    # Búsqueda lineal para recorrer las estanterías y buscar el producto
    for estanteria, productos in productos_almacen.items():
        for producto in productos:
            if producto["nombre"].lower() == nombre_producto.lower():
                cantidad_total += producto["cantidad"]
                estanterias.append(estanteria)

    # Mostrar la información
    if cantidad_total > 0:
        print(f"El producto '{nombre_producto}' está disponible en las siguientes ubicaciones:")
        for estanteria in estanterias:
            print(f" - {estanteria}")
        print(f"Cantidad total disponible: {cantidad_total} unidades")
    else:
        print(f"El producto '{nombre_producto}' no se encuentra en el almacén.")

# Ejemplo de uso:
productos_almacen = {
    "Estantería A": [{"nombre": "Chocolate Amargo", "cantidad": 20, "precio": 2.5}, {"nombre": "Mermelada de Fresa", "cantidad": 15, "precio": 3.0}], 
    "Estantería B": [{"nombre": "Aceitunas Verdes", "cantidad": 50, "precio": 1.5}, {"nombre": "Aceite de Oliva Extra", "cantidad": 10, "precio": 6.0}], 
    "Estantería C": [{"nombre": "Café Molido", "cantidad": 25, "precio": 5.0}, {"nombre": "Té Verde", "cantidad": 40, "precio": 2.0}],
    "Estantería D": [{"nombre": "Pasta Integral", "cantidad": 30, "precio": 1.8}, {"nombre": "Arroz Basmati", "cantidad": 20, "precio": 1.7}]
}

verificar_disponibilidad(productos_almacen)
