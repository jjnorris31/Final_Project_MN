import math
import numpy as np
import matplotlib.pyplot as plt


# Función de prueba
def f(c):
    return (c**3) - (7 * (c**2)) + (14 * c) - 6


x0 = 3.2  # Valores iniciales
x1 = 4

for i in range(100):

    # Comprobación inicial, si los valores iniciales x0 y x1 evaluados en la función y multiplicados entre sí
    # entonces nunca se produce un cambio de signo, por lo tanto, no hay raíz entre ese rango
    if f(x0)*f(x1) > 0:
        print("No hay raíz en este rango")

    # Primer valor y evaluación de xr
    x = (x0 + x1) / 2

    # Si el producto de fx y f1 es menor a 0, entones x0 = xr, si por el contrario es mayor o igual entonces x1 = xr
    # y el ciclo vuelve a iniciar.
    if f(x) * f(x1) < 0:
        x0 = x
    else: x1 = x

    # Condición de parada, el error es menor a .0001
    if abs(f(x)) < 0.0001:
        break

print("La raíz es: %.5f" % x0)


# Elegir valores iniciales x0 y x1, esto se puede hacer con el método gráfico
xarray = np.linspace(0, 25, 100)
yarray = np.zeros(100)

for i in range(100):
    yarray[i] = f(xarray[i])

plt.plot(xarray, yarray)
plt.grid()
