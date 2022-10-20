# set o conjuntos
# no puedes añadir mas items
# pero si puedes añadir
# no admite items repetidos
myset = {"alonso", "russel", "russel", "leclerc", "norris"}
print(type(myset))
print("Mi set tiene {} items".format(len(myset)))
print(myset)

# añadimos nuevos items
myset.add("verstappen")
print(myset)

# borramos nuestro set
myset.clear()
print(myset)