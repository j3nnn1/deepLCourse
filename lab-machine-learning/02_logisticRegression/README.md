# Regresión Logística.
* https://github.com/lab-ml-itba/Regresion-Logistica
* https://colab.research.google.com/github/lab-ml-itba/Regresion-Logistica/blob/master/0%20-%20RL%20-%20Teor%C3%ADa.ipynb#scrollTo=4wbne7JB8Z-Y
* La cross-entropy, para el caso de la regresión logística, en una función convexa y derivable
* Tiene solo un mínimo absoluto y no tiene mínimos locales

* **supuestos**:
* * * Al igual que LDA, supondremos que el logodds es lineal.
* * * Usa binary cross entropy. SI.

# Notas.
* * * En vez de maximizar la productoria. minimiza el log de la entropia - Log (L). minimiza la entropia cruzada.
* * * Es decir, la función de costo mide cuánto se parece la distribución de nuestro modelo con respecto a la real de los datos.
* * *  Se puede demostrar que la cross-entropy, para el caso de la regresión logística, en una función convexa y derivable. Ello la hace una función interesante ya que tiene solo un mínimo absoluto y no tiene mínimos locales.
* * *  J es una funcion de costo.
* * *  Parametros tita minimizar la funcion de costo (entropia cruzada.) mientras menor valor tenga mejor es el modelo.
* * *  Function J (tita): medida del error entre las anotaciones y predicciones.
* * *  Estimo parametros tita1 y tita2
* * *  tita =  W(1), titaN = W(n), tita2= W0
* * *  minimizar la distancia entre las dos distribuciones = minimizar la entropia = minimizar la divergencia KL
* * *  Busca la probabilidad que la data de entrada pertenezca a una clase positiva. Probabilidad de pertenencia a una clase y a otra clase.
* * *  Divergencia KL si la distro es igual es = a 0 por esto se usa la entropia cruzada =  H(p) + Dkl (q)