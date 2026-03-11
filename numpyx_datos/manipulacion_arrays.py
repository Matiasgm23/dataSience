import numpy as np

# --- CONCATENAR ARRAYS 1D ---
x = [1,2,3]
y = [1,2,3]
z = [1,2,3]

# Une múltiples arrays en uno solo (en línea, de corrido)
concatenarr = np.concatenate([x,y,z])
# Resultado: [1 2 3 1 2 3 1 2 3]

# --- CONCATENAR ARRAYS 2D ---
a = [[1,2],[3,4]]
b = [[5,6],[7,8]]

# axis=0 → apila por filas (uno debajo del otro)
# axis=1 → apila por columnas (uno al lado del otro)
bidimencional = np.concatenate([a,b], axis=0)
# Resultado: [[1,2],[3,4],[5,6],[7,8]]

# --- RESHAPE ---
# Reorganiza el array en la forma que le indiques (filas, columnas)
# El total de elementos debe ser el mismo: aquí 4x2 = 8 elementos
array_reformado = bidimencional.reshape(2,4)
# De forma (4,2) → pasa a forma (2,4)

# --- OPERACIONES ELEMENTO A ELEMENTO ---
array_sumado = array_reformado + array_reformado  # Suma cada elemento consigo mismo
array_multi  = array_reformado * array_reformado  # Eleva cada elemento al cuadrado

# --- RAÍZ CUADRADA ---
# Aplica √ a cada elemento del array individualmente
raices = np.sqrt(array_multi)
# Como array_multi = array_reformado², la raíz devuelve array_reformado original