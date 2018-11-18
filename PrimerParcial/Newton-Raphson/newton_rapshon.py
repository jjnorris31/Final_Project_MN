# Función original
def f(x):
    return (x ** 4) - (8.6 * (x ** 3)) - (35.51 * (x ** 2)) + (464 * x) - 998.46
# Derivada de la función original
def fprima(x):
    return (4 * (x ** 3)) - (25.8 * (x ** 2)) - (71.02 * x) + 464

x0 = 7 # Valor inicial
itera = 0 # Número de iteraciones

for i in range(100):

    itera += 1
    x1 = x0 - (f(x0) / fprima(x0))
    fx1 = f(x1) # Evaluación en la ecuación original

    if abs(fx1) < .0001: # Condición de parada
        break

    x0 = x1

print("El valor de la raiz es: %.5f"%x0)
print("Número de iteraciones: %i"%itera)