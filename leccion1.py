import pandas as pd

personas = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad': [28, 34, 29, 42],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}
indices = ['a', 'b', 'c', 'd']


df = pd.DataFrame (personas,indices)


##Sirve para poder exportar el DataFrame en un archivo CSV
df.to_csv('personas.csv')

##importar un dataframe desde un archivo CSV  el index_col=0 sirve para que la primera columna del archivo CSV se use como índice del DataFrame

import_df = pd.read_csv('personas.csv',index_col=0)


print(import_df)