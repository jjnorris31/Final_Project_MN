<h1>Eliminación Gaussiana</h1>

Este método se aplica para resolver sistemas lineales de la forma:

<a href="https://www.codecogs.com/eqnedit.php?latex=$$&space;A&space;\ast&space;B&space;=&space;B&space;$$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$$&space;A&space;\ast&space;B&space;=&space;B&space;$$" title="$$ A \ast B = B $$" /></a>

El método de eliminación Gaussiana (simple), consiste en escalonar la matriz aumentada del
sistema:

<a href="https://www.codecogs.com/eqnedit.php?latex=$$&space;(A&space;\vdots&space;B)&space;$$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$$&space;(A&space;\vdots&space;B)&space;$$" title="$$ (A \vdots B) $$" /></a>

Para obtener un sistema equivalente:

<a href="https://www.codecogs.com/eqnedit.php?latex=$$&space;a_{11}&space;&plus;&space;a_{12}&space;&plus;&space;...&space;&plus;&space;a_{1x}=&space;a_{1n}x_{n}&space;$$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$$&space;a_{11}&space;&plus;&space;a_{12}&space;&plus;&space;...&space;&plus;&space;a_{1x}=&space;a_{1n}x_{n}&space;$$" title="$$ a_{11} + a_{12} + ... + a_{1x}= a_{1n}x_{n} $$" /></a>

Donde la notación se usa simplemente para denotar que el elemento cambió. 

<a href="https://www.codecogs.com/eqnedit.php?latex=$$&space;a¿_{22}&space;&plus;&space;a_{2}&space;&plus;&space;...&space;&plus;&space;a'_{2n}x_{n}=&space;b'_{2}&space;$$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$$&space;a¿_{22}&space;&plus;&space;a_{2}&space;&plus;&space;...&space;&plus;&space;a'_{2n}x_{n}=&space;b'_{2}&space;$$" title="$$ a¿_{22} + a_{2} + ... + a'_{2n}x_{n}= b'_{2} $$" /></a>

Se despejan las incógnitas comenzando con la última ecuación y hacia arriba. Por esta
razón, muchas veces se dice que el método de eliminación Gaussiana consiste en la
eliminación hacia adelante y sustitución hacia atrás.