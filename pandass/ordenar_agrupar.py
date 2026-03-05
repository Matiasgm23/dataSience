import pandas as pd

ruta = "C:/Users/black/Downloads/Top-Películas.csv"

df  = pd.read_csv(ruta)

## .sort_values  el by hace que la columna que le pasemos
## La pone de primeras en este caso es el rating  y el ascending puede ser False o True 
## esto claramente hace que el rating pueda ir en forma ascendente o descendente

## Si queremos ordenarlos por mas de una columna lo pasamos como una lista usando ['','']
df_ordenado = df.sort_values(by=['rating','recaudación(M)'],ascending=False)

## para obetener el promedio de rating por categoria utilizamos el .groupby que agrupa en este caso el genero y obtenemos el promedio de sus rating
## con el .mean()
df_agrupado = df.groupby('género')['rating'].mean()

## Para obtener que genero recaudo mas dinero lo agrupamos por el año y obtenemos la suma total de la cantidad recaudada por año utilizando la
## Columna 'recaudacion(M)'.sum
df_recaudado = df.groupby('año')['recaudación(M)'].sum()
## Utilizamos el .sort_values(ascending=False) para poder ordenarlos descendentemente 
df_recaudado = df_recaudado.sort_values(ascending=False).head(10)

print(df_recaudado)
