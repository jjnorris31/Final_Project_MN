<h1>Euler (ecuaciones diferenciales)</h1>
Este método se basa en la misma idea del método anterior, pero hace un refinamiento en la aproximación, tomando un promedio entre ciertas pendientes. 
<p></p>
La fórmula es la siguiente: 
<p></p>
<a href="https://www.codecogs.com/eqnedit.php?latex=y_{n&space;&plus;&space;1}&space;=&space;y_{n}&space;&plus;&space;h&space;\cdot&space;\tfrac{f(x_{n},&space;y_{n})&space;&plus;&space;f(x_{n&plus;1},&space;y_{n&plus;1})}{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y_{n&space;&plus;&space;1}&space;=&space;y_{n}&space;&plus;&space;h&space;\cdot&space;\tfrac{f(x_{n},&space;y_{n})&space;&plus;&space;f(x_{n&plus;1},&space;y_{n&plus;1})}{2}" title="y_{n + 1} = y_{n} + h \cdot \tfrac{f(x_{n}, y_{n}) + f(x_{n+1}, y_{n+1})}{2}" /></a>
<a href="https://www.codecogs.com/eqnedit.php?latex=y_{n&space;&plus;&space;1}&space;=&space;y_{n}&space;&plus;&space;h&space;\cdot&space;f(x_{n},&space;y_{n})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y_{n&space;&plus;&space;1}&space;=&space;y_{n}&space;&plus;&space;h&space;\cdot&space;f(x_{n},&space;y_{n})" title="y_{n + 1} = y_{n} + h \cdot f(x_{n}, y_{n})" /></a>
<p></p>
Para entender esta fórmula, analicemos el primer paso de la aproximación, con base en la siguiente gráfica:
<p></p>
<img alt="Monografias.com" src="http://www.monografias.com/trabajos73/metodos-numericos-metodo-euler-mejorado/image007.gif" style="border:0px">
<p></p>
En la gráfica, vemos que la pendiente promedio corresponde a la pendiente de  la recta bisectriz de la recta tangente a la curva en el punto de la condición inicial y la "recta tangente" a la curva en el punto <a href="https://www.codecogs.com/eqnedit.php?latex=(x_{1},y_{1})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(x_{1},y_{1})" title="(x_{1},y_{1})" /></a> donde <a href="https://www.codecogs.com/eqnedit.php?latex=x&space;=&space;x_{1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x&space;=&space;y_{1}" title="x = x_{1}" /></a> es la aproximación obtenida con la primera fórmula de Euler. 
<p></p>
Finalmente, esta recta bisectriz se traslada paralelamente  hasta el punto de la condición inicial, y se considera el valor de esta recta en el punto <a href="https://www.codecogs.com/eqnedit.php?latex=x&space;=&space;x_{1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x&space;=&space;x_{1}" title="x = x_{1}" /></a> como la aproximación de Euler mejorada. 