#Escriba un programa que pregunte cuántos números se van a introducir, luego pida esos números, 
# y muestre un mensaje cada vez que un número no sea mayor que el anterior.

cantidad_numeros = int(input("¿Cuántos números vas a introducir? "))
anterior = float(input("Introduce el primer número: "))

for i in range(1, cantidad_numeros):
    numero = float(input("Introduce el siguiente número: "))
    if numero <= anterior:
        print("El número introducido no es mayor que el anterior.")
    anterior = numero
