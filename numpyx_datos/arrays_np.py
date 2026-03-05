import time              # Importa la librería time, sirve para medir cuánto tiempo tarda en ejecutarse algo.

import numpy as np       # Importa NumPy y lo abrevia como "np". Se usa para cálculos numéricos eficientes.


mi_array = np.array([1,2,3,4,5])  
# Crea un array de NumPy con los números 1,2,3,4,5.


print(type(mi_array))    
# Muestra el tipo de dato de mi_array (debería mostrar numpy.ndarray).


lista_grande = list(range(1000000))  
# Crea una lista de Python con números desde 0 hasta 999999 (1 millón de números).


array_grande = np.array(lista_grande)  
# Convierte la lista anterior en un array de NumPy.


print(type(lista_grande))  
# Muestra el tipo de dato de lista_grande (list).

print(type(array_grande))  
# Muestra el tipo de dato de array_grande (numpy.ndarray).


inicio_lista = time.time()  
# Guarda el tiempo actual antes de empezar el cálculo con la lista.


for i in lista_grande:
    i ** 2
# Recorre cada número de la lista y calcula su cuadrado.


fin_lista = time.time()  
# Guarda el tiempo después de terminar el cálculo.


print('Tiempo lista: ', fin_lista - inicio_lista)  
# Muestra cuánto tiempo tardó el cálculo usando la lista.


inicio_array = time.time()  
# Guarda el tiempo antes de hacer el cálculo con NumPy.


array_grande ** 2  
# Calcula el cuadrado de todos los números del array usando NumPy (vectorización).


fin_array = time.time()  
# Guarda el tiempo después del cálculo.


print('Tiempo array: ', fin_array - inicio_array)  
# Muestra cuánto tiempo tardó el cálculo usando el array de NumPy.