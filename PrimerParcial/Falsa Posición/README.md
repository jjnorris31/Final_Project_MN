<h1>Falsa posición</h1>

Después de notar que el método de bisección es un tipo de aproximación por "fuerza bruta" entonces podemos concluir que es un método relativamente ineficiente.

Su inconveniente más notable es que al dividir el intervalo de <a href="https://www.codecogs.com/eqnedit.php?latex=x_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{0}" title="x_{0}" /></a> y <a href="https://www.codecogs.com/eqnedit.php?latex=x_{1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{1}" title="x_{1}" /></a> en mitades iguales, no se toman en consideración las magnitudes de <a href="https://www.codecogs.com/eqnedit.php?latex=f(x_{0})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x_{0})" title="f(x_{0})" /></a> y <a href="https://www.codecogs.com/eqnedit.php?latex=f(x_{1})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x_{1})" title="f(x_{1})" /></a>. Si <a href="https://www.codecogs.com/eqnedit.php?latex=f(x_{0})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x_{0})" title="f(x_{0})" /></a> está más cercana a cero que <a href="https://www.codecogs.com/eqnedit.php?latex=f(x_{1})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x_{1})" title="f(x_{1})" /></a>, es lógico que la raíz e encuentre más cerca de <a href="https://www.codecogs.com/eqnedit.php?latex=f(x_{0})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x_{0})" title="f(x_{0})" /></a> que de <a href="https://www.codecogs.com/eqnedit.php?latex=x_{1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{1}" title="x_{1}" /></a>.

Lo que hace este método es unir tanto <a href="https://www.codecogs.com/eqnedit.php?latex=f(x_{0})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x_{0})" title="f(x_{0})" /></a> como <a href="https://www.codecogs.com/eqnedit.php?latex=f(x_{1})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x_{1})" title="f(x_{1})" /></a> en una línea recta, la intersección de esta línea con el eje <a href="https://www.codecogs.com/eqnedit.php?latex=x" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x" title="x" /></a> representa una mejor aproximación a la raíz. Al reemplazar la curva por una línea recta da una <i>falsa posición</i> he ahí el origen del nombre.

<a href="https://www.codecogs.com/eqnedit.php?latex=x_{r}&space;=&space;x_{1}&space;-&space;\frac{f(x_{1})(x_{0}&space;-&space;x_{1})}{f(x_{0})-f(x_{1})}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{r}&space;=&space;x_{1}&space;-&space;\frac{f(x_{1})(x_{0}&space;-&space;x_{1})}{f(x_{0})-f(x_{1})}" title="x_{r} = x_{1} - \frac{f(x_{1})(x_{0} - x_{1})}{f(x_{0})-f(x_{1})}" /></a>

o bien:

<a href="https://www.codecogs.com/eqnedit.php?latex=x_{r}&space;=&space;\frac{x_{0}f(x_{1})&space;-&space;x_{1}f(x_{0})}{f(x_{1})&space;-&space;f(x_{0})}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{r}&space;=&space;\frac{x_{0}f(x_{1})&space;-&space;x_{1}f(x_{0})}{f(x_{1})&space;-&space;f(x_{0})}" title="x_{r} = \frac{x_{0}f(x_{1}) - x_{1}f(x_{0})}{f(x_{1}) - f(x_{0})}" /></a>

Para usar este método se tiene que cumplir que:

<a href="https://www.codecogs.com/eqnedit.php?latex=f(x_{r})f(x_{1})&space;<&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x_{r})f(x_{1})&space;<&space;0" title="f(x_{r})f(x_{1}) < 0" /></a>

Al igual que en el método de bisección para actualizar el valor de <a href="https://www.codecogs.com/eqnedit.php?latex=x_{r}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{r}" title="x_{r}" /></a> tenemos que:

Si:

<a href="https://www.codecogs.com/eqnedit.php?latex=f(x_{r})f(x_{1})&space;<&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x_{r})f(x_{1})&space;<&space;0" title="f(x_{r})f(x_{1}) < 0" /></a>

entonces:

<a href="https://www.codecogs.com/eqnedit.php?latex=x_{1}&space;=&space;x_{r}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{1}&space;=&space;x_{r}" title="x_{1} = x_{r}" /></a>

Si:

<a href="https://www.codecogs.com/eqnedit.php?latex=f(x_{0})f(x_{1})&space;>&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x_{0})f(x_{1})&space;>&space;0" title="f(x_{0})f(x_{1}) > 0" /></a>

entonces:

<a href="https://www.codecogs.com/eqnedit.php?latex=x_{0}&space;=&space;x_{r}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{0}&space;=&space;x_{r}" title="x_{0} = x_{r}" /></a>

<b>Desventajas</b>

Aunque parece ser que de los métodos cerrados es el más eficiente también flaquea en algunos casos pero sobre todo falla en su <b>unitelaridad</b>. Es decir, conforme se avanza en las iteraciones, uno de los puntos limitantes del intervalo tiende a permanecer fijo, esto puede llevar a una mala convergencia, sobre todoo en funciones con una curvatura importante.
