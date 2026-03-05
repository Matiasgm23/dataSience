import pandas as pd

serie = pd.Series([5,10,15,20,25])


## Indicamos la condicion que queramos agregar a nuestra serie
filtro = serie > 15


##Aca la agregamos a nuestra serie Abriendo [], La indexamos
serie_filtrada = serie[filtro]

##Como resultado la serie solo nos mostrara los valores que sean mayor a 15
print(serie_filtrada)


serie2 = pd.Series(["banan","pera","melon","manzana"])

##No modemos aplicar metodos que van dirigidos a str a una serie por que son objetos entonces para poder solucionar eso aplicamos el
#metodo .str que nos podra servir para poder aplicar estos metodos como contains a objetos (Para resumir usando el metodo str transforma
#los objetos en str)

##El .contains nos Va a devolver valores booleanos Verdadero o falso en todos los valores de nuestra serie
filtro2 = serie2.str.contains("m")

print(filtro2)   

 


