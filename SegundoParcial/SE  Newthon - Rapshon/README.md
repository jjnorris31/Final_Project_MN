<h1>Newton - Raphson (ecuaciones no lineales)</h1>

A continuación se presenta la metodología para calcular aproximaciones de raíces de un sistema de ecuaciones no lineales.

<lo>
    <li>Se considera una primera aproximación <a href="https://www.codecogs.com/eqnedit.php?latex=x_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{0}" title="x_{0}" /></a> de la raíz de <a href="https://www.codecogs.com/eqnedit.php?latex=x_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x)" title="x_{0}" /></a></li>
    <li>Calcular <a href="https://www.codecogs.com/eqnedit.php?latex=x_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x_{0)" title="x_{0}" /></a></li>
    <li>Calcular <a href="https://www.codecogs.com/eqnedit.php?latex=x_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?df(x_{0})" title="x_{0}" /></a></li>
    <li>Obtener la solución <a href="https://www.codecogs.com/eqnedit.php?latex=\bigtriangleup&space;_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bigtriangleup&space;_{0}" title="\bigtriangleup _{0}" /></a> del sistema de ecuaciones lineales con <a href="https://www.codecogs.com/eqnedit.php?latex=df(x_{0})\bigtriangleup&space;_{0}&space;=&space;-f(x_{0})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?df(x_{0})\bigtriangleup&space;_{0}&space;=&space;-f(x_{0})" title="df(x_{0})\bigtriangleup _{0} = -f(x_{0})" /></a></li>
    <li>Obtener la aproximación <a href="https://www.codecogs.com/eqnedit.php?latex=x_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{1}" title="x_{0}" /></a> usando <a href="https://www.codecogs.com/eqnedit.php?latex=x_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{0}" title="x_{0}" /></a> y <a href="https://www.codecogs.com/eqnedit.php?latex=\Delta_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Delta_{0}" title="\Delta_{0}" /></a> mediante: <a href="https://www.codecogs.com/eqnedit.php?latex=\bigtriangleup&space;_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{1} = \bigtriangleup&space;_{0} + x_{0}" title="\bigtriangleup _{0}" /></a></li>
    <li>Repetir el proceso para obtener <a href="https://www.codecogs.com/eqnedit.php?latex=x_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{2}" title="x_{0}" /></a> usando <a href="https://www.codecogs.com/eqnedit.php?latex=x_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{1}" title="x_{0}" /></a> y los pasos anteriores.</li>
</lo>
<br>
Este proceso para una vez que se satisfagan las condiciones del error deseado.

