import pandas as pd #importamos la libreria pandas y le cambiamos el nombre a uno mas corto por pd


## Data frame es una tabla bidimensional que tiene etiquetas en filas y columnas  un data frame tiene 2 dimensiones que son el alto y el ancho
#que se indentifca por las filas y las columans
## Toma una columna por separado de esta tabla es una serie Mientraas la serie tiene solo una dimension que son sus filas por que la columna siempre va a ser una



#Creamos un diccionario para poder convertirlo en un df (DataFrame)
datos = {"nombre":["Juan","pedro","lorena"],"edad": [25,23,32]}

#Creando un data Frame o en resumen en una tabla ordenada
df = pd.DataFrame(datos)

##imprimimos para ver el dataframe
print(df)


##Si queremos trabajar con alguna serie individual podemosar usar el nombre de la variable en este caso df.nombre

print(df.nombre)




