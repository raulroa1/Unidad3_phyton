import numpy #funciones que permiten hacer tareas complejas.
lista=[1,2,3,4]
arr=numpy.array(lista)
#print(arr)
arr2=numpy.array([5,6,7,8])
#print(arr2)

#funcion con arreglo
arreglo= numpy.array([5,6,7,8,9,10,11,12])
#print(arreglo.ndim)
#print(arreglo[::2])
#arreglo1= numpy.array([0,1,2,3,4,5,6,7,8,9,10])
#c = [i for i in range(0,100,2)]
#print(c)

x=range(10)
arreglo_automatizado= [n for n in x]
print(arreglo_automatizado)