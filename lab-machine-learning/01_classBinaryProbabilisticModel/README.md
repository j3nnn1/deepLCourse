# laboratorio de machine learning.

https://dl-itba.croma.ai/courses/course-v1:itba-deeplearning+labmach+2021-T1



## Probabilisticos
Bayes, NaiveBayes, Redes Neuronales, Regresion Logística, LDA, QDA

### Modelo generativo
* Aproxima la distribucion de los datos.
* Arma modelos de los datos.
* P (X | C)

Bayes, Naive Bayes, QDA, LDA.

RC-1 . Problema 2.
De acuerdo a esta docu también están LDA y QDA:
https://www.cs.unh.edu/~mpetrik/teaching/intro_ml_17_files/class5.pdf
https://hal.inria.fr/inria-00548546/document

### Modelo Discriminativo
* Aproxima la Posteriori. Derecho la probabilidad de la clase.
* No modeliza datos.
* P (C | X)

Redes neuronales, Regresion Logistica.

### Deterministico
kNN, SVM, Arboles de decisión.

## Curso Regresión Logística, SGD Regresión Logística Repaso LDA

### Repaso LDA
* Puedo aplicar a mas de dos clases.
* Esto es un modelo generativo. porque supone que los datos fueron generados a partir de gausianas.
* Estimo el likelihood Para calcular la posteriori. likelihood es un modelo, suponiendo que pertenece a una clase.
* **Bayes**:  P (y|X) (posteriori) =( P (X|y) (likelihood) * P(y) (apriori)  ) / P(X) (constante o normalización)
* Elijo la clase que maximice la probabilidad Posteriori, cambiando por todas las clases: argmax . 
* El LogOdds es lineal. LogOdds = w Xi - C  = X transpuesta *  w vector + C = f (h) = funcion sigmoidea, h va desde - infinito a mas infinito.
* funcion sigmoidea con temperatura:  Beta = 1 / Temperatura.
*  X1 * w1 + X2 * w2 + C = 0 (sólo se da cuando las probabilidades son iguales.) por lo que se puede escribir: X2 = - X1 W1/w2 - C/W2
* suposiciones de LDA:
* * * El dataset tiene que ser linealmente separable.
* * * Los likelihoods son gaussianos.
* * * la matrix de covarianza son iguales Para todos los X (o todas las distribuciones gaussionas). (homocedasticidad)
* Regresion logistica  una evolucion de LDA?

#### Que modelos dividen el plano en una recta
* LDA.
* Regresión Logistica.

#### Que modelos dividen el plano en una cuadratica
* Bayes.
* QDA.

# Notas
(1:30:00)
Mucha descripcion de como diferenciar los modelos en la grafica con distintos datasets: 
Bayes, NaiveBayes, Redes Neuronales, Regresion Logística, LDA, QDA
https://drive.google.com/drive/folders/1aIw3dWicicbkGfm7kVyRaDSkMtvf7gBL

# Naive Gaussiano

* Puede separar distribuciones gaussianas, lineales, y es un modelo generativo.
* Si estan super puestas las clases separa bien con el smothing por defecto.(1e-09) si disminuyo  la variable de smothing
baja el score de 0.8 a 0.76

#QDA 
* Para los que son linealmente separables  tiene mayor performance que Naive  Bayes.
* es un modelo generativo.

#Regresion logistica.

# Regresion Polinomial.
## Feature engineer.
