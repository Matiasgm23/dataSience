import numpy as np

array1d = np.array([1,2,3,4,5])

array2d = np.array([[1,2,3],
                    [4,5,6],   # fila 1
                    [7,8,9]])

# --- INDEXACIÓN 1D ---
print(array1d[0])        # Elemento en posición 0 → 1

# --- INDEXACIÓN 2D ---
print(array2d[1][2])     # Fila 1, columna 2 → 6
print(array2d[0,2])      # Forma corta de lo mismo: fila 0, columna 2 → 3

# --- SLICING 1D (rebanadas) ---
# [inicio:fin] → toma desde 'inicio' hasta 'fin-1'
print(array1d[1:4])      # Posiciones 1,2,3 → [2,3,4]

# --- SLICING 2D ---
print(array2d[1, :])     # Fila 1, TODAS las columnas → [4,5,6]
print(array2d[1, 1:3])   # Fila 1, columnas 1 y 2 → [5,6]
print(array2d[:, 1])     # TODAS las filas, columna 1 → [2,5,8]
print(array2d[:2, :2])   # Filas 0-1, columnas 0-1 → [[1,2],[4,5]]

# --- FILTROS BOOLEANOS ---
# Devuelve True/False por cada elemento según la condición
print(array1d > 3)           # ¿Cuáles son mayores a 3?   → [F,F,F,T,T]
print(array2d % 2 == 0)      # ¿Cuáles son pares?         → [[F,T,F],[T,F,T],[F,T,F]]