# funciones recursivas
# funciones que se llaman asi misma
def fact(n):
    if(n <= 1):
        return 1
    else:
        return n * fact(n - 1)

print(fact(5))

# podemos hacer bucles
def bucle(i):
    if(i <= 1):
        return 1
    else:
        print(i)
        return bucle(i - 1)

bucle(10)