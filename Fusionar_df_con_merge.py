import pandas as pd

df1 = pd.DataFrame({'ID':[1,2,3],
                    'Nombre':['Ana','Luis','Carlos']})

df2 = pd.DataFrame({'ID':[1,2,4],
                    'Edad':[25,30,22]})


## .merge Sirve para unir (combinar) dos DataFrames (df1 y df2) usando una columna en común, en este caso 'ID'.

## how='outer' Sirve para unir completamente ambos DataFrames, trayendo todos los registros de df1 y todos los de df2, aunque no coincidan en el ID.
## inner → solo coincidencias

##left → todo de la izquierda

##right → todo de la derecha

##outer → todo de ambos
df_combinado = pd.merge(df1,df2, on='ID', how='outer')


print(df_combinado)