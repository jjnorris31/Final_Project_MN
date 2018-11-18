import numpy as np
import matplotlib.pyplot as plt


def y(x):
    return (2 * (x ** 2)) - (5 * x) + 3


xarray = np.linspace(-20, 20, 100)

print(xarray)

yarray = np.zeros(100)

for i in range(len(xarray)):
    yarray[i] = y(xarray[i])

plt.plot(xarray, yarray)
plt.grid()  # Muestra la cuadrícula
plt.show()  # Muestra la gráfica
