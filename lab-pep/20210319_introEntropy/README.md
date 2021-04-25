# Ejercicios prácticos desde la notebook 02-variable_aleatoria_uniforme hasta la notebook 11-Pesos-Alturas-Gaussiana

En este directorio se encuentran algunos ejercicios prácticos revisados y ejecutados del Laboratorio de probabilidad y estadistica con python.

[Repo Github con las notebooks](https://github.com/lab-pep-itba/clase-2--Probabilidad/) 

La ejecución completa de TODOS los notebooks está editada en el archivo:

* ./20200319_introEntropy/practica2_repoITBA.ipynb

## Cómo puedo samplear una variable aleatoria y además hacer un histograma para entender cual es la distribución (python). 
````
## como puedo samplear una variable aleatoria.
from matplot import pytplot as plt
import numpy as np
np.random.seed(42)
uniform_sampling = np.random.randint(1,7, 10000)
_ = plt.hist(uniform_sampling, bins=6)
````

## linspace
#### clase2.ipynb
````
import numpy as np
start = 1
stop = 10
num = 6
data = np.linspace(start, stop, num)
print(data)
````
* Data is a vector,
* Data has elements, and are evenly spaced samples (muestras espaciadas uniformemente)

## Anotaciones durante la clase.

* F función de distribución (el area puede ser mayor a 1, es la densidad acumulado)
* f función de densidad (el area debajo de la curva vale 1)
  

* **Entropía**: Es el grado de incertidumbre de la distribucion que estoy usando.
* * * A menor entropia menos preguntas tengo para hacer. más general el modelo.
* * * La medición de la entropia se usa para comparar distribuciones diferentes, con salidas diferentes o espacio muestral diferente.
* * * El espacio muestral es el mismo pero tiene diferentes distribuciones de probabilidades.
* * * Si entropia = 0 no hay incertidumbre, por lo que no es una variable aleatoria sino mas bien es deterministica.
* * * Agregar mas bolitas es agregar mas incertidumbre.
* * * Misma cantidad de bolitas de cada color acercada al numero de categorias.
* * * Teoría de la información log 1/x = log x
* * * Información = log 1/p
* * * Probabilidad * informacion = entropia
* * * tanto para variables aleatorias discretas y gaussianas continuas => se puede calcular entropia
* * * ejercicio: tengo una distribucion y nos da para calcular la entropia.
* * * Cuando disminuye la entropia disminuye la varianza o desvio standard.?? NO
* * * Hacer ejercicio que pasa con entropia y varianza cuando tenemos extremos (outliers) R= que va a pasar: entropia baja y varianza alta, poca informacion y mucha amplitud en los valores.
* * * En distribuciones que son multi modales. No se puede usar la varianza como medida de incertidumbre.
* * * Entropia cruzada para medir similitud entre distribuciones.
* * * Entropia cruzada puede ser mayor a la entropia.
* * * Dada que tengo dos distro de probabilidad la entropia cruzada mide el calculo de similitud entre dos distribuciones.
* * * entropia + divergencia KL
* * * divergencia KL = divergencia entre dos distribuciones
* * * Es la funcion de costo más usada. entropia cruzada. en deep learning y nos sirve para ver que tan bueno es nuestro modelo.
* * * La entropia de algo deterministico es 0.
* * * Mover los pesos del modelo para acercarlo a los valores del ground true (funcion de costo).