import re

# expresiones regulares
# \n salto de linea
salto_linea = re.search(r'\n', """hola 
adrian""")
print(salto_linea)

# . todo caracter menos linea nueva
punto = re.search('^Adrian', "Adrian")
print(punto)

if punto:
    print("Adrian esta en la cadena")
else:
    print("Adrian no esta en la cadena")

# ^ busca el primer caracter
primer_caracter = re.search(r'^.', "Fernando Alonso")
print(primer_caracter)

# $ busca el ultimo caracter
ultimo_caracter = re.search(r'.$', "Fernando Alonso")
print(ultimo_caracter)

# * cuantas repeticiones tiene la cadena
repeticiones = re.search(r'a+', "Fernando Alonso")
print(repeticiones)

# ahora vamos a utilizar la palabra reservada findall
# esto mostrara la los caracteres que se han encontrado
# en la cadena
cadena = "Max Verstappen es el mejor piloto de la F1 2022"
x = re.findall("Max Verstappen", cadena)
print(type(x))
if x:
    print(str(x[0]) + " es el mejor piloto y ganador de su segundo mundial")
else:
    print(x + " es un piloto de F1")

telefono = input("¿Telefono?")
print(type(telefono))
match = re.findall("[0-9]", telefono)
juntar = "".join(match)
print(juntar)
if juntar[0] == '9' or juntar[0] == '8':
    print(juntar + " es un telefono fijo")
elif juntar[0] == '6' or juntar[0] == '7':
    print(juntar + " es un telefono movil")
else:
    print("No existe este numero de telefono")