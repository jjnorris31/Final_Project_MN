def f(x): # Función de prueba
    return (x**2) - 10


def false_pos(x0, x1):

    res = 0
    iteraciones = 0

    for i in range(100):

        xr = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))
        iteraciones += 1

        if abs(f(xr)) < .0001: # Condición de parada
            break

        if f(xr) * f(x0) > 0: # Si f(x_index) tiene el mismo signo que f(a) entonces x_index ahora es a
            x0 = xr
        elif f(xr) * f(x0) < 0: # Si f(x_index) tiene el mismo signo que f(b) entonces x_index ahora es b
            x1 = xr

    return 'La raíz es: ', xr, "en: ", iteraciones, ' iteraciones.'

print(false_pos(3, 3.2)) # Caso de prueba