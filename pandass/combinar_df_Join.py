import pandas as pd

df1 = pd.DataFrame({'Salario':[30000,45000,38000],
                    'Antiguiedad':[9,13,12]},
                    index=[1,2,3])

df2 = pd.DataFrame({'Ciudad':['Madrid','Barcelona','Valencia'],
                    'Jerarquía':['Baja','Alta','Media']},
                    index=[1,2,4])



## el .join sirve En pandas, join() se usa para unir DataFrames por el índice (por defecto). Es más simple que merge() cuando trabajas con índices.
df_unido = df1.join(df2, how='inner')

print(df_unido)