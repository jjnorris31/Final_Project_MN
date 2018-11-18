def f(x):
    return ((2 * (x ** 2)) + 3) / 5


x0 = 0
iteraciones = 1

for i in range(100):

    x1 = f(x0)

    if abs(x1 - x0) < 0.0001:
        break

    x0 = x1
    iteraciones += 1

print("La raíz es: %.5f"%x1)
print("Número de iteraciones: %d"%iteraciones)
