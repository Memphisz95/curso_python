# condicionales
menor_edad = 16

if menor_edad < 18:
    print("menor de edad")

mayor_edad = 20
if mayor_edad > 18:
    print("mayor de edad")

edad = 18
frase = ""
if edad < 18:
    frase = "{} es menor de edad"
    print(frase.format(edad))
else:
    frase = "{} es mayor de edad"
    print(frase.format(edad))