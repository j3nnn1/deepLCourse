import numpy as np

¿Cuánto vale la binary cross entropy de un modelo con máxima inseguridad, sobre un dataset perfectamente balanceado?

-1*1/2*(np.log(0.5)+np.log(0.5))

¿Cuánto vale la binary cross entropy de un modelo con máxima inseguridad, sobre un dataset cuyas clases estan debalanceadas en proporciones 0.9 y 0.1?
-1 * 1/2 * (np.log(0.5) + np.log(0.5))

-1 * 0.9 * np.log(0.9) +  0.1 * np.log(0.1)

¿Cuánto vale la categorical cross entropy de un modelo con máxima inseguridad, sobre un dataset perfectamente balanceado? La cantidad de clases es 5.
-1*1/5*(np.log(0.2)+np.log(0.2)+ np.log(0.2) + np.log(0.2) + np.log(0.2))