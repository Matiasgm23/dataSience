import numpy as np  
# Importa la librería NumPy y la abrevia como "np". Se usa para trabajar con arrays y cálculos numéricos.

arrray = np.array([1,2,3])  
# Crea un array de NumPy con los números 1, 2 y 3 (array de 1 dimensión).

print(arrray.shape)  
# Muestra la forma (shape) del array.
# En este caso mostrará (3,) porque tiene 3 elementos en una sola dimensión.


array_2d = np.array([[1,2,3],[4,5,6]])  
# Crea un array de 2 dimensiones (una matriz).
# Tiene 2 filas y 3 columnas.


print(len(array_2d.shape))  
# Cuenta cuántas dimensiones tiene el array.
# array_2d.shape es (2,3) → su largo es 2 → significa que es un array de 2 dimensiones.


print(array_2d.shape)  
# Muestra la forma del array.
# (2,3) significa: 2 filas y 3 columnas.
