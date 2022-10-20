# diccionarios
# cuando creamos el diccionario
# se mantiene el orden de los items
# pero si se pueden modificar, añadir, borrar, etc
diccionario = {
    "piloto": "Fernando Alonso",
    "escuderia": "Alpine",
    "edad": "40"
}

print(diccionario)
print(type(diccionario))
print(diccionario["piloto"])

diccionario["escuderia"] = "Aston Martin"
diccionario["edad"] = 41
for i in diccionario:
    print(i, "-", diccionario[i])