# Importar pandas
import pandas as pd


# Crear 6 fechas desde 2024, una por año
fechas = pd.Series(pd.date_range('20240101', periods=6, freq='Y'))
print(fechas)


# Leer archivo CSV
ruta = 'C:/Users/pepit/Downloads/Mercado+de+Valores+España.csv'
df = pd.read_csv(ruta)


# Convertir columna 'Fecha' (texto) a fecha real
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')


# Ver tipo de dato (debería ser Timestamp)
print(type(df['Fecha'][0]))


# Obtener el mes de la segunda fecha
print(df['Fecha'][1].month)


# Extraer partes de la fecha (útil para análisis)
df['Año'] = df['Fecha'].dt.year
df['Mes'] = df['Fecha'].dt.month
df['Dia'] = df['Fecha'].dt.day


