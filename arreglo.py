import numpy as np

arr = np.array([10,20,30,40,50])

print("el arreglo es: ",arr)

print("Tipo de datos ",arr.dtype)

print("Forma de arreglo", arr.shape)

print("numero de elementos", arr.size)

print("suma 10 al arreglo", arr + 10)

print("multiplica por dos el tamaño del arreglo", arr * 2)

print("raiz cuadrada de cada elemento ", np.sqrt(arr))

print("primer elemento del arreglo ", arr[0])

print("acceder a los ultimos tres elemtos del arreglo", arr[-3:])

#cambiar el valor de un elemento 

arr[0]= 99

print("arreglo modificado ", arr[0])


