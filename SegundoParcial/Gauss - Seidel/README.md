<h1>Gauss Seidel</h1>

El método de Gauss-Seidel es el mas comúnmente usado para resolver sistemas muy grandes de ecuaciones lineales.

Comienza con una aproximación inicial <a href="https://www.codecogs.com/eqnedit.php?latex=x_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{0}" title="x_{0}" /></a> a la solución <a href="https://www.codecogs.com/eqnedit.php?latex=x,&space;y" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x,&space;y" title="x, y" /></a> genera una sucesión de vectores <a href="https://www.codecogs.com/eqnedit.php?latex=x_{k}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{k}" title="x_{k}" /></a> que convergen a la solución <a href="https://www.codecogs.com/eqnedit.php?latex=x" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x" title="x" /></a>.

Un sistema de ecuaciones algebraicas lineales es un conjunto de ecuaciones de la forma:

<a href="https://www.codecogs.com/eqnedit.php?latex=a_{11}x_{1}&space;&plus;&space;a_{12}x_{2}&plus;a_{13}x_{3}&space;&plus;&space;...&space;&plus;&space;a_{1n}x_{n}&space;=&space;b_{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a_{11}x_{1}&space;&plus;&space;a_{12}x_{2}&plus;a_{13}x_{3}&space;&plus;&space;...&space;&plus;&space;a_{1n}x_{n}&space;=&space;b_{2}" title="a_{11}x_{1} + a_{12}x_{2}+a_{13}x_{3} + ... + a_{1n}x_{n} = b_{2}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=a_{21}x_{1}&space;&plus;&space;a_{22}x_{2}&plus;a_{23}x_{3}&space;&plus;&space;...&space;&plus;&space;a_{2n}x_{n}&space;=&space;b_{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a_{21}x_{1}&space;&plus;&space;a_{22}x_{2}&plus;a_{23}x_{3}&space;&plus;&space;...&space;&plus;&space;a_{2n}x_{n}&space;=&space;b_{2}" title="a_{21}x_{1} + a_{22}x_{2}+a_{23}x_{3} + ... + a_{2n}x_{n} = b_{2}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=a_{31}x_{1}&space;&plus;&space;a_{32}x_{2}&plus;a_{33}x_{3}&space;&plus;&space;...&space;&plus;&space;a_{3n}x_{n}&space;=&space;b_{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a_{31}x_{1}&space;&plus;&space;a_{32}x_{2}&plus;a_{33}x_{3}&space;&plus;&space;...&space;&plus;&space;a_{3n}x_{n}&space;=&space;b_{2}" title="a_{31}x_{1} + a_{32}x_{2}+a_{33}x_{3} + ... + a_{3n}x_{n} = b_{2}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=a_{n1}x_{1}&space;&plus;&space;a_{n2}x_{2}&plus;a_{n3}x_{3}&space;&plus;&space;...&space;&plus;&space;a_{nn}x_{n}&space;=&space;b_{n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a_{n1}x_{1}&space;&plus;&space;a_{n2}x_{2}&plus;a_{n3}x_{3}&space;&plus;&space;...&space;&plus;&space;a_{nn}x_{n}&space;=&space;b_{n}" title="a_{n1}x_{1} + a_{n2}x_{2}+a_{n3}x_{3} + ... + a_{nn}x_{n} = b_{n}" /></a>

O bien en su forma matricial:

<a href="https://www.codecogs.com/eqnedit.php?latex={\displaystyle&space;{\begin{pmatrix}a_{11}&a_{12}&\cdots&space;&a_{1n}&space;&x_{1}&space;&b_{1}\\a_{21}&a_{22}&\cdots&space;&a_{2n}&space;&x_{2}&space;&b_{2}\\\vdots&space;&\vdots&space;&\vdots&space;&\vdots&space;&\vdots&space;&\vdots&space;\\a_{m1}&a_{m2}&\cdots&space;&a_{mn}&space;&x_{4}&space;&b_{n}\\\end{pmatrix}}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\displaystyle&space;{\begin{pmatrix}a_{11}&a_{12}&\cdots&space;&a_{1n}&space;&x_{1}&space;&b_{1}\\a_{21}&a_{22}&\cdots&space;&a_{2n}&space;&x_{2}&space;&b_{2}\\\vdots&space;&\vdots&space;&\vdots&space;&\vdots&space;&\vdots&space;&\vdots&space;\\a_{m1}&a_{m2}&\cdots&space;&a_{mn}&space;&x_{4}&space;&b_{n}\\\end{pmatrix}}}" title="{\displaystyle {\begin{pmatrix}a_{11}&a_{12}&\cdots &a_{1n} &x_{1} &b_{1}\\a_{21}&a_{22}&\cdots &a_{2n} &x_{2} &b_{2}\\\vdots &\vdots &\vdots &\vdots &\vdots &\vdots \\a_{m1}&a_{m2}&\cdots &a_{mn} &x_{4} &b_{n}\\\end{pmatrix}}}" /></a>

Que a su vez se puede expresar como:

<a href="https://www.codecogs.com/eqnedit.php?latex=Ax&space;=&space;b" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Ax&space;=&space;b" title="Ax = b" /></a>

Donde A es la matriz de coeficientes, x es el vector de incógnitas y b el vector de términos independientes.

La solución del sistema de ecuaciones es un conjunto de n valores <a href="https://www.codecogs.com/eqnedit.php?latex=x_{1},&space;x_{2},&space;x_{3},&space;...,&space;x_{n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{1},&space;x_{2},&space;x_{3},&space;...,&space;x_{n}" title="x_{1}, x_{2}, x_{3}, ..., x_{n}" /></a> que satisfacen simultáneamente todas las ecuaciones.

Tanto en el método de Gauss-Seidel como en el de Jácobi, el valor  que se le de al vector inicial carece de importancia, ya que el método convergirá a la solución rápidamente no obstante que el vector inicial tenga valores muy lejanos a la solución. Es por esto que se acostumbra a dar el vector 0 como vector inicial.
