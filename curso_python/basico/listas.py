# listas en python
# en las listas se pueden repetir valores
# se pueden cambiar valores
lista = ["primero", "segundo", "tercero", "primero"]
print(lista)
print(lista[0])

lista[0] = "cuarto"
print(lista)

print(lista[1:3])

# para insertar un valor a la lista
# indicamos lista.insert(posicion, valor)
lista.insert(0, "Vettel")
print(lista)

# añadimos al final de la lista
lista.append("Fernando Alonso")
print(lista)

# borrar items de la lista
lista.remove("cuarto")

# borrar por posicion de la lista
# si no especificamos posicion borrara
# el último item
lista.pop(2)
print(lista)

# para mostrar la lista a traves de un bucle
for i in range(len(lista)):
    print(i, "-", lista[i])

# borrar la lista completa
lista.clear()
print(lista)

pilotos = list(("Alonso", "Vettel", "Hamilton", "Verstappen", "Checo", "Russell"))
new_pilots = []
for pilot in pilotos:
    if 'a' in pilot:
        new_pilots.append(pilot) # añade solo los pilotos que contengan una 'a'

print(new_pilots)

# metodo para ordenar las listas
# lista.sort()
# OJO CON LAS MAYUSCULAS Y MINUSCULAS
# IRAN PRIMERO LAS MAYUSCULAS
pilotos.sort()
print(pilotos)

numeros = [10, 2, 46, 31, 24, 102, 120, 50]
numeros.sort(reverse = True) # ordena los numeros en orden inverso de mayor a menor
print(numeros)

f1 = pilotos.copy()
print(f1)