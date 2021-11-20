#importar bibliotecas necesarias
import pandas as pd                         # Para la manipulación y analisis de datos
import numpy as np                          # para crear vectores y matrices n-dimensionales
import matplotlib.pyplot as plt             # para generar gráficas a partir de los datos
from scipy.spatial.distance import cdist   # para el cálculo de distancias
from scipy.spatial import distance


class MDistancia():

    def __init__(self,data):
        self.data=data #variable que almacena el contenido del archivo csv

    def estandarizar_datos():
        from sklearn.preprocessing import StandardScaler, MinMaxScaler
        estandarizar = StandardScaler()                               # Se instancia el objeto StandardScaler o MinMaxScaler
        self.data = estandarizar.fit_transform(Hipoteca)         # Se calculan la media y desviación y se escalan los datos
        with popup("Metricas de distancia"):
            put_text("Los datos fueron estandarizados")

    def dataSet_info(self):
        b=self.data.info()
        return b
    #Definición de métodos para distancia Euclidiana
    def dist_euclidiana(self):
        DstEuclidiana = cdist(self.data, self.data, metric='euclidean') # mide la distancia entre los mismos elementos del data set
        MEuclidiana = pd.DataFrame(DstEuclidiana)
        return MEuclidiana

    def dist_euclidiana_rango(self,limInf,limSup):
        DstEuclidiana = cdist(self.data.iloc[limInf:limSup], self.data.iloc[limInf:limSup], metric='euclidean') # mide determinados registros entre si (limSup-limImf)
        MEuclidiana = pd.DataFrame(DstEuclidiana)
        return MEuclidiana

    def dist_euclidiana_2objetos(self,limInf,limSup): #mide la diistancia entre dos registros
        Objeto1 = self.data.iloc[limInf]
        Objeto2 = self.data.iloc[limSup]
        dstEuclidiana = distance.euclidean(Objeto1,Objeto2)
        return dstEuclidiana

    #definición de métodos para distancia chebishev
    def dist_chebishev(self):
        DstChebishev = cdist(self.data, self.data, metric='cheb')
        MChebishev = pd.DataFrame(DstChebishev)
        return  MChebishev

    def dist_cheb_rango(self,limInf,limSup):
        DstChebishev = cdist(self.data.iloc[limInf:limSup], self.data.iloc[limInf:limSup], metric='cheb')
        MChebishev = pd.DataFrame(DstChebishev)
        return MChebishev

    def dist_cheb_2objetos(self,limInf,limSup):
        Objeto1 = self.data.iloc[limInf]
        Objeto2 = self.data.iloc[limSup]
        DstChebishev = distance.chebyshev(Objeto1,Objeto2)
        return DstChebishev

    #definición de métodos para distancia manhattan
    def dist_manhattan(self):
        DstManhattan = cdist(self.data, self.data, metric = 'cityblock')
        MManhattan = pd.DataFrame(DstManhattan)
        return MManhattan

    def dist_manhattan_rango(self,limInf,limSup):
        DstManhattan = cdist(self.data.iloc[limInf:limSup], self.data.iloc[limInf:limSup], metric = 'cityblock')
        MManhattan = pd.DataFrame(DstManhattan)
        return MManhattan

    def dist_manhattan_2objetos(self,limInf,limSup):
        Objeto1 = self.data.iloc[limInf]
        Objeto2 = self.data.iloc[limSup]
        DstManhattan = distance.cityblock(Objeto1, Objeto2)
        return DstManhattan

    #definición de métodos para distancia minkowski (p = 1.5)
    def dist_minkowski(self, num):
        DstMinkowski = cdist(self.data, self.data, metric = 'minkowski', p=num ) # recomendable p = 1.5 para minkowsky
        MMinkowski = pd.DataFrame(DstMinkowski)
        return MMinkowski

    def dist_minkowski_rango(self, limInf, limSup, num):
        DstMinkowski = cdist(self.data.iloc[limInf:limSup], self.data.iloc[limInf:limSup], metric = 'minkowski', p=num)
        MMinkowski = pd.DataFrame(DstMinkowski)
        return MMinkowski

    def dist_minkowsky_2objetos(self, limInf, limSup, num):
        Objeto1 = self.data.iloc[limInf]
        Objeto2 = self.data.iloc[limSup]
        DstMinkowski = distance.minkowski(Objeto1, Objeto2, p=num )
        return DstMinkowski
