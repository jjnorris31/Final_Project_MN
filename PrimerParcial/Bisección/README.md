
<h1>Método de Bisección</h1>

También conocido como método de corte binario, de partición de intervalos o de Bolzano, es un tipo de búsqueda incremental en el que el intervalo se divide siempre a la mitad. Si la función cambia de signo sobre un intervalo, se evalúa el valor de la función en el punto medio. La posición de la raíz se determina situándola en el punto medio del subintervalo, dentro del cual ocurre un cambio de signo.

Este proceso de repite hasta obtener la mejor aproximación:

<a href="https://www.codecogs.com/eqnedit.php?latex=x_{r}&space;=&space;\frac{x_{0}&space;&plus;&space;x_{1}}{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{r}&space;=&space;\frac{x_{0}&space;&plus;&space;x_{1}}{2}" title="x_{r} = \frac{x_{0} + x_{1}}{2}" /></a>

Para usar este método se tiene que cumplir como condición inicial que:

<a href="https://www.codecogs.com/eqnedit.php?latex=f(x_{r})f(x_{1})&space;<&space;0&space;​" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x_{r})f(x_{1})&space;<&space;0&space;​" title="f(x_{r})f(x_{1}) < 0 ​" /></a>

Para actualizar el valor de <a href="https://www.codecogs.com/eqnedit.php?latex=x_{r}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{r}" title="x_{r}" /></a> tenemos que:

Si:

<a href="https://www.codecogs.com/eqnedit.php?latex=f(x_{r})f(x_{1})&space;<&space;0&space;​" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x_{r})f(x_{1})&space;<&space;0&space;​" title="f(x_{r})f(x_{1}) < 0 ​" /></a>

entonces:

<a href="https://www.codecogs.com/eqnedit.php?latex=x_{1}&space;=&space;x_{r}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{1}&space;=&space;x_{r}" title="x_{1} = x_{r}" /></a>

Si:

<a href="https://www.codecogs.com/eqnedit.php?latex=f(x_{r})f(x_{1})&space;>&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x_{r})f(x_{1})&space;>&space;0" title="f(x_{r})f(x_{1}) > 0" /></a>

entonces:

<a href="https://www.codecogs.com/eqnedit.php?latex=x_{0}&space;=&space;x_{r}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{0}&space;=&space;x_{r}" title="x_{0} = x_{r}" /></a>

Este método puede ser muy tardado por lo que más adelante se presentará el método de la falsa posición.
