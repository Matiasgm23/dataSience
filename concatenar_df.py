import pandas as pd

df1 = pd.DataFrame({'Nombre':['Juan','Gabriela','Elena'],
                    'Edad':[23,31,21]})


df2 = pd.DataFrame({'Nombre':['Carmela','Max','Laura'],
                    'Edad':[34,25,29]})


## .concat Sirve para poder unir una tabla (DataFrame) debajo de la otra  y si usamos el parametro axis = 1 las tablas se van a unir en forma
# horizontal y si es = 0 se unen en vertical  
# Si queremos el indice vaya en orden es de decir 1,2,3,4,5.... usaremos el parametro ignore_index = True



df_cancatenado = pd.concat([df1,df2], axis=0, ignore_index=True)

# si queremos ver el indice origina y a que df pertenece cada uno de ellos ocupamos el parametro keys=['df1','df2']
# Podemos elejir nombres que nos parescan mas significativos.
df_cancatenado2 = pd.concat([df1,df2], keys=['df1','df2'])




print(df_cancatenado2)