def estado_almacen(productos_almacen):
    total_productos = 0
    valor_total = 0.0

    print("Estado del almacén:")

    for estanteria, productos in productos_almacen.items():
        cantidad_estanteria = sum(producto["cantidad"] for producto in productos)
        valor_estanteria = sum(producto["cantidad"] * producto["precio"] for producto in productos)
        total_productos += cantidad_estanteria
        valor_total += valor_estanteria

        print(f"\n{estanteria}:")
        print(f"  - Cantidad total de productos: {cantidad_estanteria} unidades")
        print(f"  - Valor total de productos: {valor_estanteria:.2f} euros")
        for producto in productos:
            print(f"    - {producto['nombre']}: {producto['cantidad']} unidades, {producto['precio']} euros/unidad")

    print(f"\nTotal de productos en el almacén: {total_productos} unidades")
    print(f"Valor total del inventario: {valor_total:.2f} euros")

# Ejemplo de uso:
productos_almacen = {
    "Estantería A": [{"nombre": "Chocolate Amargo", "cantidad": 20, "precio": 2.5}, {"nombre": "Mermelada de Fresa", "cantidad": 15, "precio": 3.0}], 
    "Estantería B": [{"nombre": "Aceitunas Verdes", "cantidad": 50, "precio": 1.5}, {"nombre": "Aceite de Oliva Extra", "cantidad": 10, "precio": 6.0}], 
    "Estantería C": [{"nombre": "Café Molido", "cantidad": 25, "precio": 5.0}, {"nombre": "Té Verde", "cantidad": 40, "precio": 2.0}],
    "Estantería D": [{"nombre": "Pasta Integral", "cantidad": 30, "precio": 1.8}, {"nombre": "Arroz Basmati", "cantidad": 20, "precio": 1.7}]
}

estado_almacen(productos_almacen)
