import pandas as pd

datos_clima = pd.read_csv("C:/Users/pepit/Downloads/Precipitaciones.csv")


head_df = datos_clima.head(1)
tail_df = datos_clima.tail(1)

print(head_df , tail_df)