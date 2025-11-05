import pandas as pd

empleados = {"nombre":["Ana","Luis","Carlos"],"edad":[30,25,40]}

df_empleados = pd.DataFrame(empleados)


edades = df_empleados.edad



print(edades)