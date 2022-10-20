# vamos a llamar al modulo calculadora para tener todas
# las operaciones disponibles en este archivo
import calculadora as calc

a = 10
b = 2
print(calc.suma(a, b))
print(calc.resta(a, b))
print(calc.multiplicar(a, b))
print(calc.dividir(a, b))
print(calc.potencia(a, b))
print(calc.resto(a, b))

# para importar modulos que estan en otras carpetas
# nombreCarpeta.nombreCarpeta.nombreModulo