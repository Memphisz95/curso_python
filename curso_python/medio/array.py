# vamos a importar el modulo array
import array as arr

# para crear un array
numeros = arr.array('i', [10, 20, 30])
print(numeros)
print(type(numeros))
print(len(numeros))
print(numeros.index(20)) # muestra la posicion del item

# podemos recorrer el array con un bucle
for i in range(len(numeros)):
    print(numeros[i])

# los array son mutables y se pueden cambiar el valor de los items
numeros[0] = 40
print(numeros)