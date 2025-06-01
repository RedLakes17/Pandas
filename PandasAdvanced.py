#Primero creemos un dataframe a partir de un diccionario
import pandas as pd
import numpy as np

Perros_dic={"Nombre":["Beta","Ogui","Pao","Chestnut","Cookie","Apolo","Sasha"], "Color":["Cafe","Blanco","Miel","Negro","Negro","Miel","Cafe"], "Peso_kg":[35,3,20,15,38,22,35]}
Perros=pd.DataFrame(Perros_dic)




'''Cosas basicas'''

#Agregar una columna
Perros["Altura_cm"]=[80,30,60,62,84,62,74]
Perros["Raza"]=["Dobermann","Poodle","Electrico","Cocker","Dobermann","Electrico","Pastor"]
Perros["Altura_m"]=Perros["Altura_cm"]/100
Perros["Comida_por_semana"]=[4,1,2,2,5,3,4]

#Ordenar el dataframe
Perros=Perros.sort_values(["Altura_cm","Peso_kg"], ascending=False)

#Subsetting
Perros[(Perros["Color"]=="Miel") & (Perros["Color"]=="Cafe")] #Si son cafe o miel
Es_Dober_O_Elect=Perros["Raza"].isin(["Dobermann","Electrico"]) #Si son electricos o doberman
Perros[Perros["Color"]=="Negro"]["Peso_kg"] #Peso de perros color negro

print(Perros)





'''Summary Statistics'''

#Para columnas numericas
print("Promedio del peso:", Perros["Peso_kg"].mean()) #median, mode, min, max, var, std, sum, quantile

#The .agg() method
def ComidaTotal(columna):
    return columna.sum()
print("Comida total consumida:",Perros["Comida_por_semana"].agg(ComidaTotal))

#Suma acumulativa
Perros["Comida_por_semana"].cumsum()





'''Counting'''

#Para eliminar duplicados en alguna columna
Perros.drop_duplicates(["Color"])
#Para tener en cuenta mas caracteristicas
Perros.drop_duplicates(subset=["Color","Peso_kg"])

#Para contar cuantas repeticiones hay en una columna
Perros["Color"].value_counts() #Normalize, Sort son algunos parametros para ordenar la salida






'''Grouped summary statistics'''

#Para tomar el promedio de cierta caracteristica numerica de los valores repetidos de una columna
print("Promedio del peso de perros del mismo color:",Perros.groupby("Color")["Peso_kg"].mean())

#Usando el agg() method para obtener diferentes estadisticas
Perros.groupby("Color")["Altura_cm"].agg([max, min, sum])

#Cual es el dobermann cafe mas pesado?
print(Perros.groupby(["Color","Raza"])[["Peso_kg","Nombre"]].max())



'''Pivot tables'''

#Para hacer lo mismo que la primera linea del apartado anterior pero con una pivottable
print(Perros.pivot_table(values="Peso_kg",index="Color")) #Por defecto saca el promedio mean
Perros.pivot_table(values="Peso_kg",index="Color", aggfunc=np.median) #Para una funcion diferente




'''Explicit indexes'''

#Para hacer que una columna sea el indice
Perros=Perros.set_index("Nombre")
Perros=Perros.reset_index()
#print(Perros)

#Se pueden poner mas de dos indices
Perros=Perros.set_index(["Nombre","Raza"])

#Para seleccionar columnas e indices
Perros=Perros.iloc[2:4,1:3]

