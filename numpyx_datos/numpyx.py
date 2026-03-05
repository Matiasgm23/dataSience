import numpy as np      # Importa la librería NumPy y la abrevia como "np". Se usa para cálculos numéricos.

import pandas as pd     # Importa la librería Pandas y la abrevia como "pd". Se usa para trabajar con tablas de datos.

ruta = "C:/Users/pepit/Downloads/Ciudades_Visitadas_Latinoamerica_2023.csv"  
# Guarda la ruta del archivo CSV donde están los datos.

df = pd.read_csv(ruta)  
# Lee el archivo CSV y lo convierte en un DataFrame (tabla de datos en pandas).

promedio = df['Población'].mean()  
# Calcula el promedio (media) de la columna "Población".

redondear = np.round(df['Población'].mean())  
# Calcula el promedio de la población y lo redondea al número entero más cercano usando NumPy.

minimo = np.min(df['Visitantes'])  
# Obtiene el valor mínimo de la columna "Visitantes".

maximo = np.max(df['Visitantes'])  
# Obtiene el valor máximo de la columna "Visitantes".

print(maximo)  
# Muestra en pantalla el valor máximo de visitantes.

