<h1>Método Newton-Raphson</h1>

Si el valor inicial para la raíz es <a href="https://www.codecogs.com/eqnedit.php?latex=x_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{0}" title="x_{0}" /></a> entonces se puede trazar una tangente desde el punto <a href="https://www.codecogs.com/eqnedit.php?latex=[x_{i},&space;f(x_{i})]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?[x_{i},&space;f(x_{i})]" title="[x_{i}, f(x_{i})]" /></a> de la curva. El punto en donde esta tangente cruza al eje x representa una aproximación mejorada de la raíz.

<i>Fórmula de Newton-Rapshon</i>:

<a href="https://www.codecogs.com/eqnedit.php?latex=x_{i&space;&plus;&space;1}&space;=&space;x_{i}&space;-&space;\frac{f(x_{i})}{f'(x_{i})}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{i&space;&plus;&space;1}&space;=&space;x_{i}&space;-&space;\frac{f(x_{i})}{f'(x_{i})}" title="x_{i + 1} = x_{i} - \frac{f(x_{i})}{f'(x_{i})}" /></a>

<b>Desventajas</b>

Por lo general es muy eficiente excepto en dos casos:
<ul>
    <li>Raíces múltiples</li>
    <li>Algunas raíces simples</li>
</ul>

Un ejemplo es cuando se nos pide determinar la raíz positiva de <a href="https://www.codecogs.com/eqnedit.php?latex=f(x)&space;=&space;x^{10}&space;-&space;1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;x^{10}&space;-&space;1" title="f(x) = x^{10} - 1" /></a> con un valor inicial de <a href="https://www.codecogs.com/eqnedit.php?latex=x&space;=&space;0.5" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x&space;=&space;0.5" title="x = 0.5" /></a>.

La fórmula a utilizar es:

<a href="https://www.codecogs.com/eqnedit.php?latex=x_{i&space;&plus;&space;1}&space;=&space;x_{i}&space;-&space;\frac{x_{i}^{10}&space;-&space;1}{x_{i}^{9}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{i&space;&plus;&space;1}&space;=&space;x_{i}&space;-&space;\frac{x_{i}^{10}&space;-&space;1}{x_{i}^{9}}" title="x_{i + 1} = x_{i} - \frac{x_{i}^{10} - 1}{x_{i}^{9}}" /></a>

Con esta fórmula sí que llegamos a un valor correcto pero después de iterar bastantes veces:

<div align="center">
    <img src=https://image.ibb.co/hssXKe/Captura.png>
</div>

No hay un criterio general de convergencia para este método. Su convergencia depende de la naturaleza de la función y de la exactitud del valor inicial.

Ten en cuenta que para algunas funciones <b>ningún</b> valor inicial funcionará, una solución para esto es diseñar un programa que sea capaz de detectar la convergencia lenta o la divergencia.