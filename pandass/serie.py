import pandas as pd 

df = pd.read_csv("C:/Users/pepit/Downloads/Precipitaciones.csv")


## Una serie de pandas es un arreglo unidimencional  es decir de una sola dimension y que es capaz de almacenar cualquier tipo de dato
serie = df["region"]
print(serie.head())


#Creamos una lista normal para poder transformarla en una serie de pandas

datos = [1,2,3,4,5]

##Con el .Series podemos transformar una lista normal en una serie de pandas una serie unidimencional
serie2 = pd.Series(datos)

indices = ["a","b","C","d","e"]

##Podemos Cambiarle los indices a nufestros datos siempre cuando el numero de indices coincida con el numero todal de datos 
serie3 = pd.Series(datos,indices)




print(serie3)


#Creando un diccionario de paises con sus capitales
capitales = {
    "chile": "Santiago",
    "argentina":"Buenos aires",
    "brazil":"brazilia",
    "peru":"Lima"
}


## en un Diccionario se comporta diferente la key  vendria siendo el indice y el  value , vendria siendo  el dato 
serie4  = pd.Series(capitales)






print(serie4)