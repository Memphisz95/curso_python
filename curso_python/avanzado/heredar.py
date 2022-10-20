# heredar clases
class Animal:
    nombre = ""

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre del animal: {self.nombre} - Edad del animal: {self.edad}"

# -------------------------------------------------------------------------------------------------------------------------
# creamos otra clase para saber el tipo de animal
class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

class Gato(Animal):
    pass

# -------------------------------------------------------------------------------------------------------------------------
# instanciamos las clases
leon = Animal("Spike", 20)
labrador = Perro("Choco", 1)
blanco = Gato("Blanquito", 4)

print(leon)
print(labrador)
print(blanco)