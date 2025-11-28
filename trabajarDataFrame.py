import pandas as pd

data = {
    'Nombre':['Ana','Luis','Carlos','Sara'],
    'Edad':[25,30,22,27],
    'Ciudad':['Madrid','Barcelona','Valencia','Bilbao']

}

df = pd.DataFrame(data)

## Para poder agregar una columna a nuestro dataFrame debemos hacerlo asi 
df['Salario']=[30000,40000,38000,32000]

## Para poder modificar una columna de nuestro dataFrame debemos llamar a nuestra columna y modificarla en este caso la columna salario
##le aumentamos 2000 a todos los salarios 
df['Salario']= df['Salario'] + 2000


## Para poder trabajar con una serie en particular
nombres = df['Nombre']

## Para poder mostrar a las personas que sean mayor a 25 
mayores_de_25 = df[df['Edad'] > 25]






print(mayores_de_25)


