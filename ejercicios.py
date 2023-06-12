import numpy as np #aqui se le dice que importe de la galeria numpy, y que valga np.

numero_random=np.random.randint(0,100)#buscar numero random
print(numero_random)

x=range(0,10)#aqui se pone un rango
arreglo=np.array(x)#aqui le decimos al arreglo es del tamaño del rango
for n in x:
    arreglo[n]=np.random.randint(0,100)#aqui se le dice al arreglo que cada vez que pase por el for agarre un numero aleatorio
print(arreglo)#aqui se printea el arreglo para comprobar.
print("el numero mas grande:",arreglo.max())#printear el numero mas grande del arreglo
print("el numero mas pequeño:",arreglo.min())#printear el numero mas pequeño del arreglo
print("la suma de todos los elementos:",arreglo.sum())#printear la suma de los elementos del arreglo
print("el numero mas grande:",arreglo.mean())#printear el promedio del arreglo