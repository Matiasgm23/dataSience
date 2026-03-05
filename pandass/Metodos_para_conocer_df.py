import pandas as pd

##Crear una dataFrame a partir de un Archivo csv ## Siempre para poner la ruta del archivo porne el /
df = pd.read_csv("C:/Users/pepit/Downloads/Precipitaciones.csv")





##el .head nos va a mostar las primero 5 lineas de nuestro dataframe ademas le puedo pasar la cantidad de filas que quiero que me muestre


## el .tail() nos muestra los ultimos 5 registros de nuestro data frame 

## el .shape() nos muestra la cantidad de filas y columnas que tiene nuestro dataframe

## el .columns nos devolvera una lista con los encabezados de las columnas

## el .info() nos devuelve informacion importante del data frame

## eñ .describe() nos va a devolver informacion resumida de las columnas numericas como el conteo , promedio,  min , max etc



print(df.describe())