import pandas as pd

# Crear DataFrame con índice personalizado
df = pd.DataFrame({
    'Col1': [100, 200, 300],
    'Col2': [400, 500, 600],
    'Col3': [700, 800, 900]
}, index=['fila1', 'fila2', 'fila3'])

# 1️⃣ Seleccionar filas específicas por nombre
print("Filas fila1 y fila3:")
print(df.loc[['fila1', 'fila3']])
print()

# 2️⃣ Seleccionar rango de filas (incluye ambos extremos)
print("Desde fila2 hasta fila3:")
print(df.loc['fila2':'fila3'])
print()

# 3️⃣ Selección con máscara booleana manual
print("Máscara booleana [False, True, False]:")
print(df.loc[[False, True, False]])
print()

# 4️⃣ Filtrar filas donde Col1 > 150
print("Filas donde Col1 > 150:")
print(df.loc[df['Col1'] > 150])
print()

# 5️⃣ Seleccionar columnas específicas
print("Solo columnas Col1 y Col2:")
print(df.loc[:, ['Col1', 'Col2']])




# ================================
# RESUMEN .loc vs .iloc en Pandas
# ================================

# 🔹 .loc
# Se usa para seleccionar datos usando el NOMBRE de las filas o columnas.
# Es decir, trabaja con las etiquetas (labels) del DataFrame.
# Cuando usamos rangos, incluye el último valor.

# Ejemplos:
df.loc['fila1']                  # Selecciona la fila llamada 'fila1'
df.loc[:, 'Col1']                # Selecciona la columna 'Col1'
df.loc['fila1':'fila3']          # Selecciona desde fila1 hasta fila3 (incluye fila3)
df.loc[df['Col1'] > 150]         # Filtra filas según una condición


# 🔹 .iloc
# Se usa para seleccionar datos usando la POSICIÓN numérica.
# Funciona como si las filas y columnas estuvieran numeradas desde 0.
# Cuando usamos rangos, NO incluye el último valor.

# Ejemplos:
df.iloc[0]        # Primera fila (posición 0)
df.iloc[:, 1]     # Segunda columna (posición 1)
df.iloc[0:2]      # Desde la primera hasta antes de la tercera


# 🧠 Diferencia fácil de recordar:
# loc  → trabaja con nombres
# iloc → trabaja con números