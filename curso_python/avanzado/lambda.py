# funciones anonimas
x = lambda piloto: f"El piloto es: {piloto}"
print(x("Hamilton"))
print(x("Albon"))

# lambdas dentro de funciones
def apellido(a):
    return lambda n: f"El piloto es: {n} {a}"

piloto_1 = apellido("Russel")
print(piloto_1("George"))