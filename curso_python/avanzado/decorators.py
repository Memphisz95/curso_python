# constiste en crear una funcion
# e introducirla en una variable
# por ejemplo
def numero(n):
    return n

funcion_numero = numero
print(funcion_numero(5))

# podemos crear funciones dentro de funciones
def nombre(n, a):
    def apellido(a):
        return n + " " + a
    
    result = apellido(a)
    return result

print(nombre("Fernando", "Alonso"))

# podemos crear una funcion que tenga como parametro
# otra funcion
def piloto(n):
    return n

def parrilla(piloto):
    p1 = "Verstapen"
    p2 = "Russel"
    p3 = "Leclerc"
    return (f"p1 - {p1} \n p2 - {p2} \n p3 - {p3}")

print(parrilla(piloto))