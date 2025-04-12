import numpy as np
list=[2,34.23,65,7,3,"hola que hace",46,7, True] #Las listas pueden tener varios tipos de varibles al mismo tiempo
lista1=np.array([[1,2,3],[4,5,6],[7,8,9]]) #Los arrays solo tienen un tipo de varible
print(lista1[:,:])

print(list.index("hola que hace"))

#El ciclo for puede recorrer listas con listas
casa=[["cocina", 123],["cuarto 1", 43],["cuarto 2", 32],["baño", 54]]
for x,y in casa:
    print("La/El "+str(x)+" mide "+str(y)+" metros cuadrados.")