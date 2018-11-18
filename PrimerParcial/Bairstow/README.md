<h1>Bairstow</h1>

Es un método iterativo relacionado de alguna manera con los métodos de Müller y Newton-Raphson, para motivos ilustrativos tenemos que recordar que:

<a href="https://www.codecogs.com/eqnedit.php?latex=f_{5}(x)&space;=&space;(x&plus;1)(x-4)(x-5)(x&plus;3)(x-2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_{5}(x)&space;=&space;(x&plus;1)(x-4)(x-5)(x&plus;3)(x-2)" title="f_{5}(x) = (x+1)(x-4)(x-5)(x+3)(x-2)" /></a>

Si se divide entre un factor que no es una raíz, el cociente es un polinomio de 4to grao pero habrá un residuo diferente de 0. A partir de aquí podemos elaborar un algoritmo para determinar la raíz de un polinomio.

<ol>
    <li>De un valor inicial para la raíz x = t</li>
    <li>Divida el polinomio entre el factor x-t</li>
    <li>Determine si hay un residuo diferente de 0, si este existe, ajuste el valor inicial en forma sistemática y repita el procedimiento hasta       que el residuo desapareza y se localice en la raíz</li>
    <li>Una vez hecho el paso 4, repite el procedimineto totalmente, ahora el cociente podrá determinar otra raíz</li>
</ol>


Relación de recurrencia simple para realizar la división entre el factor cuadrático:

<a href="https://www.codecogs.com/eqnedit.php?latex=b_{n}&space;=&space;a_{n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?b_{n}&space;=&space;a_{n}" title="b_{n} = a_{n}" /></a>
<br>
<a href="https://www.codecogs.com/eqnedit.php?latex=b_{n&space;-1}&space;=&space;a_{n-1}&space;&plus;&space;rb_{n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?b_{n&space;-1}&space;=&space;a_{n-1}&space;&plus;&space;rb_{n}" title="b_{n -1} = a_{n-1} + rb_{n}" /></a>
<br>
<a href="https://www.codecogs.com/eqnedit.php?latex=b_{i}&space;=&space;a_{i}&space;&plus;&space;rb_{i&plus;1}&space;&plus;&space;sb_{i&plus;2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?b_{i}&space;=&space;a_{i}&space;&plus;&space;rb_{i&plus;1}&space;&plus;&space;sb_{i&plus;2}" title="b_{i} = a_{i} + rb_{i+1} + sb_{i+2}" /></a>


Si las derivadas parciales de las b, pueden determinarse, hay un sistema de dos ecuaciones que se resuelve simutáneamente pra las dos incógnitas, <a href="https://www.codecogs.com/eqnedit.php?latex=\Delta{r}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Delta{r}" title="\Delta{r}" /></a> y <a href="https://www.codecogs.com/eqnedit.php?latex=\Delta{s}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Delta{s}" title="\Delta{s}" /></a>. Las derivadas parciales se obtienen por división sintética de las b en forma similar a como las b fueron obtenidas:

<a href="https://www.codecogs.com/eqnedit.php?latex=c_{n}&space;=&space;b_{n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?c_{n}&space;=&space;b_{n}" title="c_{n} = b_{n}" /></a>
<br>
<a href="https://www.codecogs.com/eqnedit.php?latex=c_{n&space;-1}&space;=&space;b_{n-1}&space;&plus;&space;rc_{n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?c_{n&space;-1}&space;=&space;b_{n-1}&space;&plus;&space;rc_{n}" title="c_{n -1} = b_{n-1} + rc_{n}" /></a>
<br>
<a href="https://www.codecogs.com/eqnedit.php?latex=c_{i}&space;=&space;b_{i}&space;&plus;&space;rc_{i&plus;1}&space;&plus;&space;sc_{i&plus;2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?c_{i}&space;=&space;b_{i}&space;&plus;&space;rc_{i&plus;1}&space;&plus;&space;sc_{i&plus;2}" title="c_{i} = b_{i} + rc_{i+1} + sc_{i+2}" /></a>

Es aquí donde las derivadas parciales se sustituyen en las ecuaciones junto con las b para dar:


<a href="https://www.codecogs.com/eqnedit.php?latex=c_{2}\Delta{r}&space;&plus;&space;c_{3}\Delta{s}&space;=&space;-&space;b_{1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?c_{2}\Delta{r}&space;&plus;&space;c_{3}\Delta{s}&space;=&space;-&space;b_{1}" title="c_{2}\Delta{r} + c_{3}\Delta{s} = - b_{1}" /></a>
<br>
<a href="https://www.codecogs.com/eqnedit.php?latex=c_{1}\Delta{r}&space;&plus;&space;c_{2}\Delta{s}&space;=&space;-&space;b_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?c_{1}\Delta{r}&space;&plus;&space;c_{2}\Delta{s}&space;=&space;-&space;b_{0}" title="c_{1}\Delta{r} + c_{2}\Delta{s} = - b_{0}" /></a>

Cuando ambos errores estimados caen por debajo del criterio especificado, los valores de las reaíces se determinan mediante:

<a href="https://www.codecogs.com/eqnedit.php?latex=x&space;=&space;\frac{r&space;&plus;-&space;\sqrt{r^{2}&space;&plus;&space;4s}}{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x&space;=&space;\frac{r&space;&plus;-&space;\sqrt{r^{2}&space;&plus;&space;4s}}{2}" title="x = \frac{r +- \sqrt{r^{2} + 4s}}{2}" /></a>

De aquí en adelante existen sólo 3 posibilidades:

<ol>
    <li><b>El cociente es un polinomio de tercer grado o mayor.</b> En tal caso, el método de Bairstow se aplica al cociente para evaluar un nuevo valor de r y s. Los valores anteriores de r y s pueden servir como valores iniiales en esta aplicación.</li>
    <li><b>El cociente es cuadrático.</b> Aquí es posible evaluar directamente la dos raíces restantes con la ecuación cuadrática.</li>
    <li><b>El cociente de un polinomio de primer grado.</b> En este caso, la raíz restante se evalúa simplemente como <a href="https://www.codecogs.com/eqnedit.php?latex=x&space;=&space;-\frac{s}{r}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x&space;=&space;-\frac{s}{r}" title="x = -\frac{s}{r}" /></a>.</li>
</ol>