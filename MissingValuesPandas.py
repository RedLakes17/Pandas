"""Missing values"""
import pandas as pd

Perros_dic={"Nombre":["Beta","Ogui","Pao","Chestnut","Cookie","Apolo","Sasha"], "Color":["Cafe","Blanco","Miel","Negro","Negro","Miel","Cafe"], "Peso_kg":[35,3,20,15,38,22,35]}
Perros=pd.DataFrame(Perros_dic)
#Agregar columnas
Perros["Altura_cm"]=[80,30,60,62,84,62,74]
Perros["Raza"]=["Dobermann","Poodle","Electrico","Cocker","Dobermann","Electrico","Pastor"]
Perros["Altura_m"]=Perros["Altura_cm"]/100
Perros["Comida_por_semana"]=[4,1,2,2,5,3,4]


#Para detectar si hay valores faltante
print(Perros.isna()) #Para cada dato
print(Perros.isna().sum()) #Para cada columna

#Para graficar los valores faltantes
Perros.isna().sum().plot(kind="bar")

#Para elimiar cualquier fila (registro) con valores faltantes
Perros.dropna()

#Pare reemplazar los valores faltantes
Perros.fillna(0)
