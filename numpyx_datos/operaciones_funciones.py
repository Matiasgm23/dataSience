import numpy as np

# =============================================
# BROADCASTING EN NUMPY
# =============================================
# Broadcasting permite operar arrays de distintas formas.
# NumPy "estira" el array más pequeño para que encaje con el grande.

array1 = np.array([1, 2, 3])          # Shape: (3,)     → 1 fila, 3 columnas
array2 = np.array([[0],[10],[20],[30]]) # Shape: (4, 1)  → 4 filas, 1 columna

# NumPy combina ambos shapes → resultado de shape (4, 3)
# Cada fila de array2 se suma/multiplica con todos los elementos de array1
broadcast_suma  = array1 + array2   # [[1,2,3], [11,12,13], [21,22,23], [31,32,33]]
broadcast_multi = array1 * array2   # [[0,0,0], [10,20,30], [20,40,60], [30,60,90]]

print(broadcast_multi)

# =============================================
# OPERACIONES ARITMÉTICAS CON np.ufuncs
# =============================================
# NumPy tiene funciones universales (ufuncs) para operar elemento a elemento.
# Son equivalentes a los operadores +, -, *, / pero más explícitas y extensibles.

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

resultado = np.add(a, b)       # [5, 7, 9] — equivale a a + b
# Otras operaciones del mismo tipo:
## np.subtract(a, b)  → resta        → a - b
## np.multiply(a, b)  → multiplicación → a * b
## np.divide(a, b)    → división      → a / b

# =============================================
# FUNCIONES MATEMÁTICAS ELEMENTO A ELEMENTO
# =============================================

resultado2 = np.exp(a)     # e^x para cada elemento  → [e^1, e^2, e^3] ≈ [2.71, 7.38, 20.08]
print(resultado2)

resultado3 = np.log(a)     # Logaritmo natural (base e) → [ln(1), ln(2), ln(3)] ≈ [0, 0.69, 1.09]
print(resultado3)

resultado4 = np.log10(a)   # Logaritmo en base 10 → [log10(1), log10(2), log10(3)] ≈ [0, 0.30, 0.47]
print(resultado4)

resultado5 = np.sqrt(a)    # Raíz cuadrada → [√1, √2, √3] ≈ [1, 1.41, 1.73]
print(resultado5)
