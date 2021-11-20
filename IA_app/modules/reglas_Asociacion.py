import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from apyori import apriori
from pywebio.output import *

listaM=[]
ItemsLista=[]
class Reglas_Asociacion():

    def __init__(self,data):
        self.data = data

    def dataSet_info(self):
       return self.data.info

    def exploracion(self):
        global listaM,ItemsLista
        transacciones=self.data.values.reshape(-1).tolist()  ## -1 es dimensión no conocida
        listaM=pd.DataFrame(transacciones)
        listaM['Frecuencia'] = 0
        #Se agrupa los elementos
        listaM = listaM.groupby(by=[0], as_index=False).count().sort_values(by=['Frecuencia'], ascending=True) #Conteo
        listaM['Porcentaje'] = (listaM['Frecuencia'] / listaM['Frecuencia'].sum()) #Porcentaje
        listaM = listaM.rename(columns={0 : 'Item'})

        ItemsLista = self.data.stack().groupby(level=0).apply(list).tolist()

        return listaM, ItemsLista

    def reporte_Apriori(self, soporte, confianza, elevacion):
        global listaM,ItemsLista
        # 0.01 , 0.3, 2 |
        soporte= round(soporte/len(self.data),2 )
        Reglas = apriori(ItemsLista,
                        min_support=soporte,
                        min_confidence=confianza,
                        min_lift=elevacion)

        Resultados = list(Reglas)

        put_markdown(f"### Se encontraron {len(Resultados)} reglas\n")
        put_text("----------------------------------------------------------")
        characters = "frozenset"
        for item in Resultados:
            emparejar = item[0]
            items = [x for x in emparejar]
            string = str(item[0])
            string = re.sub("frozenset","",string)
            put_text("Regla: {}".format(string))
            put_text("Soporte: {:.3}".format(float(str(item[1]))))
            put_text("confianza: {:.3}".format(float(str(item[2][0][2]))))
            put_text("Lift: {:.3}\n".format(float(str(item[2][0][3]))))
            put_text("----------------------------------------------------------")
