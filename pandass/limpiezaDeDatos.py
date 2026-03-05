
import pandas as pd

##Hacer la limpieza de datos es importante por que evita errores, mejora la precision del analisis y asegura resultados confiables


##Creamos un diccionario con diferentes campos con sus respecticos key value
data  = {
    'Id_producto':[1001,1002,1003,1003],
    'Cantidad_vendida':[30,None,25,25],
    'Precio':[20.5,10.0,None,22.5]
}

df = pd.DataFrame(data)


## .isnull() nos devuelve valores booleanos si es verdadero es que hay valores nulos y  si es falso  no hay 

## isnull().sum() Nos va a devolver por cada columna cuantos null tiene

##OPCIONES PARA ARREGLAR LOS VALORES NULL

#1- .dropna() Sirve para poder eliminar todos los valores nulos de el dataFrame
df_eliminados = df.dropna()

#2- .fillna() Sirve para poder rellenar los valores nullos por algun valor que nosotros queramos en este caso es 0
df_rellenados = df.fillna({"Cantidad_vendida":0,"Precio":df["Precio"].mean()})

#3- .astype(int) Sirve para poder cambiar el tipo de dato si tenemos un dato float y queremos cambiarlo a int asi podemos cambiarlo
df_rellenados["Cantidad_vendida"] = df_rellenados["Cantidad_vendida"].astype(int)


#4- .drop_duplicates() Sirve para poder eliminar los duplicados de una columna pero si no le pasamos parametros tiende a buscar duplicados
#Completos que se dupliquen en todas las columnas pero si le pasamos como parametro una columna ahi si podra eliminar los duplicados
#de esa columna
df_unicos = df_rellenados.drop_duplicates(subset="Id_producto")



  




print(df_unicos)






