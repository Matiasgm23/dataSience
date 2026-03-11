import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9])

# --- RESHAPE ---
# Reorganiza el array en (filas, columnas) — total elementos debe ser igual
arrya_mod = array.reshape(3, 3)
# [1,2,3,4,5,6,7,8,9] → [[1,2,3],
#                          [4,5,6],
#                          [7,8,9]]

# -1 significa "calcula tú solo cuántas filas necesitas"
# NumPy deduce: 9 elementos / 3 columnas = 3 filas
array_mod2 = array.reshape(-1, 3)   # Resultado idéntico al de arriba

# --- TRANSPOSE ---
# Gira el array: las filas se vuelven columnas y viceversa
array_volteado = array_mod2.transpose()
# [[1,4,7],
#  [2,5,8],
#  [3,6,9]]

# --- FLATTEN vs RAVEL ---
# Ambos convierten cualquier array multidimensional en 1D (una sola fila)
array_chato = arrya_mod.flatten()  # Devuelve una COPIA (cambios no afectan al original)
array_ravel  = arrya_mod.ravel()   # Devuelve una VISTA (cambios SÍ afectan al original)

print(array_ravel)  # [1,2,3,4,5,6,7,8,9]