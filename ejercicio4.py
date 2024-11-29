


colores_lista = ["rojo", "verde", "azul", "amarillo"]
print("Lista de colores:", colores_lista)
print("Primer color en la lista:", colores_lista[0])  # Acceder al primer elemento


numeros_suerte_tupla = (7, 13, 21, 33)
print("Tupla de números de la suerte:", numeros_suerte_tupla)
print("Último número en la tupla:", numeros_suerte_tupla[-1])  # Acceder al último elemento


dias_favoritos_conjunto = {"lunes", "viernes", "domingo"}
print("Conjunto de días favoritos:", dias_favoritos_conjunto)

dia_verificado = "viernes"
if dia_verificado in dias_favoritos_conjunto:
    print(f"El día {dia_verificado} está en el conjunto de días favoritos.")
else:
    print(f"El día {dia_verificado} no está en el conjunto de días favoritos.")


precios_productos = [15.99, 25.50, 9.99, 40.00, 12.75]
print("Lista de precios:", precios_productos)


print("Precio del primer producto:", precios_productos[0])
print("Precio del tercer producto:", precios_productos[2])
print("Precio del último producto:", precios_productos[-1])


umbral_precio = 30.00
if any(precio > umbral_precio for precio in precios_productos):
    print(f"Existen productos con precios mayores a {umbral_precio}.")
else:
    print(f"Todos los precios son menores o iguales a {umbral_precio}.")
