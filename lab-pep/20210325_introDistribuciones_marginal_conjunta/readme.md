
# Apuntes de la clase sobre La distribucion de la variable aleatoria.

## Notebook: 05-Pesos-Alturas-Marginal


distribucion marginales = (1 sola variable aleatoria)

distribucion conjunta = (dos variables al mismo tiempo (Peso 65 y altura 160 i.e.) o 3 o mas variables)

* Distribucion NO parametrizada . (categorica no aproximada)
  Se usa cuando no se sabe que distribucion siguen los datos.
  Al calculo a traves de los datos de la probabilidad individual. 
  Es lo que llama *estimacion de la probabilidad*.
  *aproximacion de la probabilidad*
  Cuando hago sampling a partir del espacio muestral y las probabilidades calculadas anteriormente des los datos discretos.
  
* cuanto mas parametros tengo que estimar, necesito mas datos para estimar.

* Distribucion conjunta:

Pasos:
Dataset > estimacion de la conjunta > genero mas observaciones con random.choice > lo graficamos y vemos si es similar.

Probabilidad condiciona es filtro el dataset por todas las condiciones que aparecen antes del |
y el calculo se hace en funcion del subconjunto generado.
* Como paso de conjunta a marginal.
* si tengo la conjunta tengo TODO. Da mas informacion que las marginales.
* necesitas un volumen da datos bien grande para estimar la conjunta.
Que no haya correlacion lineal no implica que las variables sean independiente. Puede tener correlacion cuadratica.
* correlacion lineal.
* correlacion cuadratica.
* Vector de medias define la matrix de covarianza contiene la relacion entre todas las variables.
La diagonal de la matrix de covarianza es la varianza.
* si normalizo la matrix de covarianza se llama matrix de correlacion.
* covarianza -1 a 1, si es 0 no tiene relacion lineal, puede que sea independiente.
* normal (media, desviacion std)
* tratar el ejercicio pesos alturas como continua. (vector de mdias, matrix covarianza)
* MAtrix de covarianza de una gaussiana.
una gausiana multivariable en el problema de las imagenes.
si suponemos que se puede describir con una conjunta multivariable.
variables a estimar = 784 * 784
* software: REVISE => REveling  Visual BiaSEs, usa un nivel de abstraccion distinto.
* La conjunta no la tenemos en la mayoria de los casos lo que hacemos
aproximamos la conjunta a partir de las marginales.
* naive bayes.
* Cual es la diferencia aca:
    NO SUPONGO INDEPENDENCIA.
    ASUMIR independencia y NO asumir indenpendencia da resultados similares. 
  
* Tipos de modelos de Naive Bayes.
* como armo un modelo para un texto.

* ley de probabilidad total, es una forma de calcular la marginal.
Probabilidad conjunta  = P ( A interseccion Bi) = P (A) = sumatoria i=1 a k de P (A | Bi) * P (Bi)
  si Bi son mutuamente excluyentes
  y exhaustivos (la suma de todos da igual a 1)
en el denominador aplico probabilidad total.
  

filtros de kalman.
cuanto combustible le tienes que meter a un cohete.
gps sincronizacion gracias a los filtros de kalman.




