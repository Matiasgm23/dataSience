import pandas as pd

##Crear el data frame

df_empleados  = pd.DataFrame({
    'nombre':["Ana","Luis","Carlos"],
    'edad':[30,25,40]
})

## explorar los atributos principales


shape_df = df_empleados.shape
columns_df = df_empleados.columns
index_df = df_empleados.index


##imprimir los resultados

print("shape del dataframe", shape_df)
print("Columans del dataFrame", columns_df)
print("Indice del dataframe", index_df)


