import pandas as pd

numeros = pd.Series([10,20,30,40,50])

promedio = numeros.mean()

print(f"el promedio es {promedio}")


total = numeros.sum()

print(f"la suma total de los numeros es {total}")


maximo = numeros.max()
print(f"el maximo de los numeros es {maximo}")


minimo = numeros.min()

#tenemos muchos metodos de agregacion como el .mean() que nos va a devolver el  promedio de la serie , .sum() que nos va a devolver el
#total de la serie sumada  , el .max() que nos va a devolver el numero maximo o mas grande de la serie 
# y por ultimo el .min() que nos devolverra el numero minimo de la serie


#existen otros metodos utilies igual como .median() para poder encontrar la media  y .std para poder encontrar desviacion estandar


mediana = numeros.median()

desviacion  = numeros.std()