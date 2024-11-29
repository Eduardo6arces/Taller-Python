
for contador in range(5):
    print("python")


limite_superior = int(input("Ingresa un número límite para generar una secuencia del 1 hasta ese valor: "))

if limite_superior < 1:
    print("Por favor, ingresa un número mayor o igual a 1.")
else:
    print(f"Generando números del 1 al {limite_superior}:")
    for numero in range(1, limite_superior + 1):
        print(numero)


valor_limite = int(input("Ingresa un número límite para generar los números pares desde 0: "))

if valor_limite < 0:
    print("Por favor, ingresa un número mayor o igual a 0.")
else:
    print(f"Números pares desde 0 hasta {valor_limite}:")
    for numero_par in range(0, valor_limite + 1, 2):
        print(numero_par)


if valor_limite % 2 == 0:
    print(f"El límite ingresado {valor_limite} es par.")
else:
    print(f"El límite ingresado {valor_limite} es impar.")
