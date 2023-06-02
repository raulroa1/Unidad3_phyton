import numpy as np

numero_random=np.random.randint(0,100)
print(numero_random)

x=range(0,10)
arreglo=np.array(x)
for n in x:
    arreglo[n]=np.random.randint(0,100)
print(arreglo)
    