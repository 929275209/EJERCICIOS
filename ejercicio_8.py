#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
# la primera letra la letra que se encuentra en medio y la ultima letra separadas por comas(,).

palabra = input("Introduce una palabra: ")

longitud = len(palabra)
primera_letra = palabra[0]
ultima_letra = palabra[-1]

if longitud % 2 == 0:
    letra_media = palabra[longitud // 2 - 1]
else:
    letra_media = palabra[longitud // 2]

print("Las letras extremas de la palabra '{}' son: {}, {}, {}".format(palabra, primera_letra, letra_media, ultima_letra))
