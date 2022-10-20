# tuplas
# se pueden repetir pero no se pueden modificar
# el orden de los items
tuplas = ("alonso", "vettel", "hamilton", "vettel")
print(tuplas)

# para modificar tuplas primero tenemos
# que convertir en lista
# modificamos y luego volvemos a pasar
# a tupla

lista = list(tuplas)
print(type(lista))

# modificamos la posicion que queramos
lista[0] = "fernando"
tuplas = tuple(lista)
print(tuplas)

# de igual forma para añadir o borrar items con append
i = 0
while i < len(tuplas):
    print(tuplas[i])
    i += 1