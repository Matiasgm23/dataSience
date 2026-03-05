import pandas as pd

##Creamos una serie 
serie = pd.Series([10,20,30,40,50])

##A la serie en su indice 0 que el valor que corresponde es 10 le vamos a sumar 10 mas en total quedaria 20 
##A esto se le llama indexar
serie[0] = serie[0] + 10


##para poder sumarle a todos 10 o el numero que quisieramos podriamos tomar serie en general y agregarle 10
serie  = serie + 10


##Asi mismo podriamos restarle o multiplicar un valor o a todos los valores de la serie 
serie = serie * 10 

serie = serie / 10 




##Imprimimos serie con los cambios ya hechos 
print(serie)