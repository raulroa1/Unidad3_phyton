import numpy as np
arreglo=np.array([4,8,15,16,23,42])
contar_hasta=len(arreglo)
for i in range(contar_hasta):
    #imprimiendo uno por uno el arreglo
    print(arreglo[i])
#imprimiendo el arreglo original
print(arreglo)
#crear acceso directo a un arreglo
arreglo_copia=arreglo[:]

#cambio el original
#arreglo[0]=3
#arreglo_copia[2]=100
#print("original", arreglo)
#print("copia", arreglo_copia)

arreglo_copia=arreglo[:].copy()
arreglo[0]



