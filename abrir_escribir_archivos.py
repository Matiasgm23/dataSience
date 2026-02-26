# Importa la librería pandas y la renombra como pd (estándar en Data Science)
import pandas as pd

# Rutas donde están los archivos que quiero leer
ruta_excel = 'C:/Users/pepit/Downloads/Compras_desde_ads.xlsx'
ruta_xml = 'C:/Users/pepit/Downloads/Valores+de+acciones.xml'

# Lee un archivo Excel y lo guarda en un DataFrame (tabla)
df1 = pd.read_excel(ruta_excel)

# Lee un archivo XML y lo guarda en un DataFrame
df2 = pd.read_xml(ruta_xml)

# Diccionario con distintos tipos de datos
numeros = {
    'romanos': ['I', 'II', 'III', 'IV'],      # Números romanos
    'arabigos': [1, 2, 3, 4],                 # Números normales
    'texto': ['uno', 'dos', 'tres', 'cuatro'] # Números escritos
}

# Convierte el diccionario en un DataFrame
df = pd.DataFrame(numeros)

# Crea una nueva columna llamada 'Fechas'
# pd.date_range genera 4 fechas seguidas desde 01-01-2024
df['Fechas'] = pd.Series(pd.date_range('20240101', periods=4))

# Guarda el DataFrame en un archivo Excel
# index=False evita que se guarde la columna índice
df.to_excel('C:/Users/pepit/Downloads/numeros.xlsx', index=False)

# Muestra en pantalla los DataFrames leídos y el creado
print(df1, df2, df)