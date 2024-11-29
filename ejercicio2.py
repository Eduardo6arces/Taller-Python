
numero_ingresado = int(input("Ingresa un número para verificar si es par o impar: "))

if numero_ingresado % 2 == 0:
    print(f"El número {numero_ingresado} es par.")
else:
    print(f"El número {numero_ingresado} es impar.")


limite_verificacion = 20
if numero_ingresado > limite_verificacion:
    print(f"El número {numero_ingresado} es mayor que {limite_verificacion}.")
elif numero_ingresado < limite_verificacion:
    print(f"El número {numero_ingresado} es menor que {limite_verificacion}.")
else:
    print(f"El número {numero_ingresado} es igual a {limite_verificacion}.")


categoria_producto = input("Ingresa la categoría del producto (A, B o C): ").upper()

if categoria_producto == "A":
    print("El producto pertenece a la categoría A: Alta calidad.")
elif categoria_producto == "B":
    print("El producto pertenece a la categoría B: Calidad estándar.")
elif categoria_producto == "C":
    print("El producto pertenece a la categoría C: Calidad económica.")
else:
    print("Categoría no válida. Por favor, elige A, B o C.")
