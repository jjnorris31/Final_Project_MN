<h1>Factorización LU</h1>

La factorización LU es una forma de factorización de una matriz como el producto de una matriz triangular inferior y una superior. 

Sea A una matriz no singular:

<a href="https://www.codecogs.com/eqnedit.php?latex={\displaystyle&space;A=LU\,}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\displaystyle&space;A=LU\,}" title="{\displaystyle A=LU\,}" /></a>

donde L y U son matrices inferiores y superiores triangulares respectivamente.

Para matrices <a href="https://www.codecogs.com/eqnedit.php?latex=$$&space;3&space;\times&space;3$$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$$&space;3&space;\times&space;3$$" title="$$ 3 \times 3$$" /></a>, esto es:

<a href="https://www.codecogs.com/eqnedit.php?latex={\displaystyle&space;{\begin{pmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\\\end{pmatrix}}={\begin{pmatrix}1&0&0\\l_{21}&1&0\\l_{31}&l_{32}&1\\\end{pmatrix}}{\begin{pmatrix}u_{11}&u_{12}&u_{13}\\0&u_{22}&u_{23}\\0&0&u_{33}\\\end{pmatrix}}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\displaystyle&space;{\begin{pmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\\\end{pmatrix}}={\begin{pmatrix}1&0&0\\l_{21}&1&0\\l_{31}&l_{32}&1\\\end{pmatrix}}{\begin{pmatrix}u_{11}&u_{12}&u_{13}\\0&u_{22}&u_{23}\\0&0&u_{33}\\\end{pmatrix}}}" title="{\displaystyle {\begin{pmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\\\end{pmatrix}}={\begin{pmatrix}1&0&0\\l_{21}&1&0\\l_{31}&l_{32}&1\\\end{pmatrix}}{\begin{pmatrix}u_{11}&u_{12}&u_{13}\\0&u_{22}&u_{23}\\0&0&u_{33}\\\end{pmatrix}}}" /></a>

Por otro lado la descomposición PLU tiene esta forma:

<a href="https://www.codecogs.com/eqnedit.php?latex={\displaystyle&space;L_{m-1}P_{m-1}...L_{2}P_{2}L_{1}P_{1}A=U}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\displaystyle&space;L_{m-1}P_{m-1}...L_{2}P_{2}L_{1}P_{1}A=U}" title="{\displaystyle L_{m-1}P_{m-1}...L_{2}P_{2}L_{1}P_{1}A=U}" /></a>


Para determinar L:

<a href="https://www.codecogs.com/eqnedit.php?latex={\displaystyle&space;L=({L'}_{m-1}*...*{L'}_{2}*{L'}_{1})^{-1}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\displaystyle&space;L=({L'}_{m-1}*...*{L'}_{2}*{L'}_{1})^{-1}}" title="{\displaystyle L=({L'}_{m-1}*...*{L'}_{2}*{L'}_{1})^{-1}}" /></a>

y cada <a href="https://www.codecogs.com/eqnedit.php?latex={\displaystyle&space;{L'}_{k}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\displaystyle&space;{L'}_{k}}" title="{\displaystyle {L'}_{k}}" /></a> está dado por:

<a href="https://www.codecogs.com/eqnedit.php?latex={\displaystyle&space;{L'}_{k}}&space;=&space;{\displaystyle&space;{P}_{m-1}*...*{P}_{k&plus;1}*{L}_{k}*{P^{-1}}_{k&plus;1}*...*{P^{-1}}_{m-1}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\displaystyle&space;{L'}_{k}}&space;=&space;{\displaystyle&space;{P}_{m-1}*...*{P}_{k&plus;1}*{L}_{k}*{P^{-1}}_{k&plus;1}*...*{P^{-1}}_{m-1}}" title="{\displaystyle {L'}_{k}} = {\displaystyle {P}_{m-1}*...*{P}_{k+1}*{L}_{k}*{P^{-1}}_{k+1}*...*{P^{-1}}_{m-1}}" /></a>

