'''Joining tables'''
import pandas as pd

#Creemos dos tablas con dos diccionarios
ColoniasBJ={'numero':['1','2','3','4','5'],
            'nombre':['Postal','Alamos','Narvarte','Ninos heroes','Roma'],
            'direccion':['alicante 151','galicia 45','morena 38','tuy 201','xola 114'],
             'zip':['03410','52303','65078','21789','56978'] }
ColoniasBJPoblacion={'numero':['1','2','3','4','5'],
                    'pop_2000':[15234,35644,45677,34567,65435],
                    'pop_2010':[23674,39698,65322,45675,78904],
                    'direccion':['alicante 34','galicia 66','morena 12', 'tuy 234','xola 73'],
                    'zip':['03410','52303','65078','21789','56978']}

ColBJ1=pd.DataFrame(ColoniasBJ)
ColBJ_pop=pd.DataFrame(ColoniasBJPoblacion)



'''Basico'''
#Para combinar dataframes
Combinar=ColBJ1.merge(ColBJ_pop, on='numero', suffixes=('_1','_2')) #Solo aparecen los registros que estan en las columnas numero de ambos dataframes. Interseccion entre los circulos
Combinar=Combinar.set_index('numero')#Para cambiar el indice
print(Combinar.head())
#Para unir tablas con mas de una columna
Combinar2=ColBJ1.merge(ColBJ_pop, on=['numero', 'zip'])

'''Left joins''' #union de tablas en las que se muestran todos los registros de la tabla izquierda y los registros de la tabla derecha que coinciden con la izquierda(todo el circulo izquierdo coloreado en un diagrama de venn)
Combinar=ColBJ1.merge(ColBJ_pop, on='numero', how='left') #se puede reemplazar left por right, inner o outer para diferentes tipos de uniones
#Para unir tablas respecto a dos columnas con nombre diferente
Combinar=ColBJ1.merge(ColBJ_pop, left_on='numero', right_on='zip', how='left')

'''Vertical joins'''
#pd.concat([, ignore_index=True])