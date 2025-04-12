import pandas as pd

#Crear dataframes
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
# Create dictionary my_dict with three key:value pairs: my_dict
my_dict={'country':names, 'drives_right':dr, 'cars_per_cap':cpc}
# Build a DataFrame cars from my_dict: cars
cars=pd.DataFrame(my_dict)
# Print cars
print(cars)
# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
# Specify row labels of cars
cars.index=row_labels
# Print cars again
print(cars)

#Para ver las primeras filas(vistazo rapido al datagrame)
print(cars.head()) #metodo
#Para ver las columnas del dataframe
print(cars.info())
#Para ver caracteristicas de columnas numericas
print(cars.describe())
#Para mostrar el dataframe en un arreglo numpy
print(cars.values) #atributo
print(cars.columns)
print(cars.index)

#To select especific information from the dataFrame
print(cars[["country", "cars_per_cap"]]) #Columnas
print(cars[2:5]) #Filas


#loc and iloc functions
print(cars.loc[["IN", "JPN"],["country", "cars_per_cap"]]) #select columns and rows
print(cars.iloc[[2,3],[1,2]]) #With iloc function we use the indexes of the tags insted of the tags

#Para obtener info con comparaciones
MuchosCarros=cars["cars_per_cap"]>500
print(cars[MuchosCarros])

#Usando comparaciones y logica
import numpy as np
MuchPocosCarros=np.logical_or(cars["cars_per_cap"]>500, cars["cars_per_cap"]<50)
print(cars[MuchPocosCarros])

#Para un ciclo for usamos el iterrows method
for lab, row in cars.iterrows():
    print(str(lab)+": "+str(row["country"]))

#Funcion apply para crear mas columnas a partir de aplicar una funcion a otra columna
cars["NameLength"]=cars["country"].apply(len)
print(cars)


