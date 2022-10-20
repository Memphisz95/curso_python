# para crear una clase utilizaremos
# la palabra reservada class
class Piloto:

    edad = 0 # atributo de la clase

# metodo constructor
    def __init__(self, nom, escuderia):
        self.nom = nom
        self.escuderia = escuderia

# creamos metodos para mostrar el objeto
# se puede sustituir por el metodo __str__
# para mostrar directamente sin llamar el metodo
    def descripcion(self):
        return f"{self.nom} esta en la escuderia {self.escuderia}"

    def podios(self, p):
        return f"{self.nom} tiene {p} podios"

# ----------------------------------------------------------------------------------------------------------------------------------
# creamos la instancia
primer_piloto = Piloto("Fernando Alonso", "Alpine")
print(primer_piloto.nom) # para mostrar el valor del item
print(primer_piloto.descripcion())
print(primer_piloto.podios(120))