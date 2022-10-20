# trabajamos con cadenas
# slicing

cadena = "paLaBRa"
print(cadena[1:6])

# pasar a mayusculas la variable
print(cadena.upper())

# pasar a minusculas la variable
print(cadena.lower())

# borrar espacios en blanco desde adelante
espacios = "    - hello,  world!"
print(espacios.strip())

# reemplazar palabra o letra
print(cadena.replace("p", "N"))

# separar en un array las palabras
frase = "Me gusta,  mucho el futbol"
print(frase.split(","))

# para concatenar dos string
edad = 27
nom_edad = "Mi nombre es Adrian y tengo {}"
print(nom_edad.format(edad))