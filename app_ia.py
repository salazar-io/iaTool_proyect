from pywebio import *
from pywebio.input import *
from pywebio.output import *
import plotly.express as px
import time
import pandas as pd
from modules import *

#from metricas_distancia import *
#from reglas_Asociacion import *


description =r'''
Esta es una web app construida como proyecto final para la asignatura de Inteligencia Artificial, FI UNAM
Hecho con [pyweb.io](https://pyweb.io)
------------
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():

    session.set_env(title='IA TOOL')
    with popup("❤ Bienvenido a IA TOOL"):
        put_text("Hecho por Edgar Salazar Serrano \nGithub: @salazar-io")

    put_markdown('# 🤖 Análisis de datos con inteligencia artificial 💻' )
    put_markdown(description)
    inicio()
    session.hold()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
def medic():
    with use_scope('scope_principal',clear=True):
        toast("Analisis de datos médicos")

        sel = select("Seleccione analisis", ['metricas de distancia', 'clustering', 'pronóstico'])
        put_text(f"Has escogido {sel}. Por favor, espera.")
        cargando()

        if sel == 'metricas de distancia':
            put_text("metricas de distancia")

            return_inicio()

        elif sel== 'clustering':
            put_text("Clustering")

            return_inicio()

        else:
            put_text("pronóstico")
            return_inicio()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def hipoteca():

    with use_scope('scope_principal',clear=True):
        toast('Analisis de datos hipotecarios')

        sel = select("Seleccione analisis", ['metricas de distancia', 'clustering', 'pronóstico'])
        put_text(f"Has escogido {sel}. Por favor, espera.")
        cargando()

        if sel == 'metricas de distancia':

            put_text("metricas de distancia")
            df = pd.read_csv('Data/Hipoteca.csv')
            metricas=MDistancia(df)
            eucl= metricas.dist_euclidiana_rango(100,105)
            eucl = pd.DataFrame(eucl)
            put_text("Distancias: \n")
            #put_html( df.to_html(show_dimensions = True, max_rows = 10 ))
            put_html(eucl.to_html(max_rows=20,show_dimensions=True))

            return_inicio()
        elif sel== 'clustering':
            put_text("Clustering")

            return_inicio()
        else:
            put_text("pronóstico")

            return_inicio()


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def store():

    with use_scope('scope_principal',clear=True):
        toast("Analisis de ventas en tienda🛒")
        sel = select("Seleccione tipo de analisis", ['Reglas de asociación','Metricas de distancia', 'Clustering', 'Pronóstico'])
        put_text(f"Has escogido {sel}. Por favor, espera.")
        cargando()

        df = pd.read_csv("Data/store_data.csv")
        put_markdown("##    Productos vendidos en una semana")
        texto_Data = "estos datos representan los productos que se vendieron en una semana... bla bla bla"
        muestra_data(texto_Data,df)


        if sel == 'Metricas de Distancia':
            put_text("Metricas de distancia ")

            return_inicio()

        elif sel == 'clustering':
            put_text("Clustering")

            return_inicio()

        elif sel == 'Reglas de asociación':
            r_asociacion(df)

            return_inicio()

        else:
            put_text("pronóstico")
            return_inicio()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def movies():

    with use_scope('scope_principal',clear=True):
        toast("Análisis de películas vistas 🎞")

        sel = select("Seleccione tipo de analisis", ['Reglas de asociación','Metricas de distancia', 'Clustering', 'Pronóstico'])
        put_text(f"Has escogido {sel}. Por favor, espera.")
        cargando()

        df = pd.read_csv("Data/movies.csv")
        put_markdown("##    Peliculas vistas en una semana")
        texto_Data = "estos datos representan las peliculas que fueron vistas por los usuarios..."
        muestra_data(texto_Data,df)

        if sel == 'Metricas de Distancia':
            put_text("Metricas de distancia ")

            return_inicio()

        elif sel == 'clustering':
            put_text("Clustering")

            return_inicio()

        elif sel == 'Reglas de asociación':
            r_asociacion(df)

            return_inicio()

        else:
            put_text("pronóstico")
            return_inicio()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##Funcionamiento de la app

def inicio():
    with use_scope('scope_principal',clear=True):
        put_markdown("### Haga click en un grupo de interés para comenzar")
        put_grid([
        [put_markdown("### Datos Médicos "),put_image('https://www.pixelstalk.net/wp-content/uploads/images1/Medical-Wallpapers-HD-Free-download-768x443.jpg', title='Datos médicos', width='80%' ).onclick(medic)],
        [put_markdown("### Datos de Hipoteca "),put_image('https://cdn.hipwallpaper.com/i/85/97/AML6VS.jpg', title='Datos de hipoteca', width='80%').onclick(hipoteca)],
        [put_markdown("### Datos de peliculas vistas "),put_image('https://www.desophict.com/wp-content/uploads/2020/09/netflix-wallpaper-1536x1012.webp', title='Datos de peliculas', width='80%').onclick(movies)],
        [put_markdown("### Datos de ventas en una tienda  "),put_image('https://kochgenossen.com/wp-content/uploads/2016/09/prosi_innen1-1200x630-cropped.jpg', title='Datos de tienda', width='80%').onclick(store)]
        ])

def return_inicio():
        put_markdown('## Volver al inicio ').onclick(inicio)

def cargando():
    with use_scope('scope_principal',clear=True):
        put_processbar('bar')
        for i in range(1, 11):
            set_processbar('bar', i / 10)
            time.sleep(0.15)
    clear_barra()

def clear_barra():
    clear('scope_principal')

#--------------------------------------------------------------------------------------------------------------------------------------
## mostar y esconder datos
def muestra_data(texto_Data, df):
    with use_scope('scope_data', clear = True):
        put_text(texto_Data)
        put_html(df.to_html(max_rows=10,show_dimensions=True, border=0))
        put_button('Esconder datos',onclick= lambda: hide(1,texto_Data,df))


def hide(a,texto_Data,df):
     clear(scope='scope_data')
     if a :
         with use_scope('scope_data', clear = True):
             put_button('Mostrar datos',onclick= lambda: muestra_data(texto_Data,df))
#--------------------------------------------------------------------------------------------------------------------------------------
def r_asociacion(df):
    rA = Reglas_Asociacion(df)
    a,b = rA.exploracion()
    with use_scope('r_asociacion', clear= True):
        config = input_group("configuración del algoritmo Apriori",[
            input("Ingrese el soporte",name="soporte", type=NUMBER, validate=check_num),
            input("Ingrese la confianza",name = "confianza", type=FLOAT, validate=check_num),
            input("Ingrese la elevación",name = "lift", type=FLOAT, validate=check_num)
        ])

        #210,0.3,0.01
        rA.reporte_Apriori(config["soporte"], config["confianza"], config["lift"])

def check_num(p):  # return None when the check passes, otherwise return the error message
    if p < 0:
        return 'intente de nuevo'

main()
