'''Opciones avanzadas de matploylib con pandas'''
import matplotlib.pyplot as plt
plt.ion()
import pandas as pd

Perros_dic={"Nombre":["Beta","Ogui","Pao","Chestnut","Cookie","Apolo","Sasha"], "Color":["Cafe","Blanco","Miel","Negro","Negro","Miel","Cafe"], "Peso_kg":[35,3,20,15,38,22,35]}
Perros=pd.DataFrame(Perros_dic)
#Agregar columnas
Perros["Altura_cm"]=[80,30,60,62,84,62,74]
Perros["Raza"]=["Dobermann","Poodle","Electrico","Cocker","Dobermann","Electrico","Pastor"]
Perros["Altura_m"]=Perros["Altura_cm"]/100
Perros["Comida_por_semana"]=[4,1,2,2,5,3,4]


#Histograma
Perros["Altura_cm"].hist()
plt.savefig("HistogramaAdvancedPdPlt.png")
plt.clf()

#Grafico de sliced dataframes
avg_weight_by_breed=Perros.groupby("Raza")["Peso_kg"].mean()
avg_weight_by_breed.plot(kind="bar", title="Peso medio de cada raza")
plt.savefig("AdvecedGraficaRazaPeso.png")




