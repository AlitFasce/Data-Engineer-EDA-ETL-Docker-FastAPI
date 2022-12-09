#librerias a importar_las mismas tambien estan en el archivo requierments del docker
import pandas as pd

#************************************ QUERYS**************************************************

#DISPONIBILIZANDO csv
df_visual_l=pd.read_csv("visualgeneral.csv")

#   QUERY1
def get_max_duration(anio,plataforma,min_o_season):

    plataforma=str(plataforma)

    plataforma=plataforma.lower()
    anio=int(anio)

    maximo=0
    
    df_tvshow=(df_visual_l[(df_visual_l.platform==plataforma)&(df_visual_l.release_year==anio)&(df_visual_l.type=='TV Show')]).drop_duplicates(subset='title')
    
    df_movie=(df_visual_l[(df_visual_l.platform==plataforma)&(df_visual_l.release_year==anio)&(df_visual_l.type=='Movie')]).drop_duplicates(subset='title')
        
    if min_o_season=='seasson':
        maximo=df_tvshow.dur_time.max()
    elif min_o_season=='min':
        maximo=df_movie.dur_time.max()
        
    df_rta=(df_movie[(df_movie.dur_time==maximo)]) 
    lista_rta=[]
    for i in df_rta['title']:
        lista_rta.append(i)
        t=lista_rta[0]
    x=f'el título que más se repite es {t}'
    return x

#   QUERY2
def get_count_plataform(plataforma):


    plataforma=plataforma.lower()
    df_movie=(df_visual_l[(df_visual_l.platform==plataforma)&(df_visual_l.type=='Movie')])   #.drop_duplicates(subset='title')

  
    df_tvshow=(df_visual_l[(df_visual_l.platform==plataforma)&(df_visual_l.type=='TV Show')])     #.drop_duplicates(subset='title')
    
    p= df_movie.title.count()

    s=df_tvshow.title.count()

    n=f'la cantidad de peliculas es de {p} y la de series es de {s}, por la plataforma solicitada, {plataforma}'
        
    return n

#   QUERY3
def get_listedin(genero):
    
    genero=str(genero.capitalize())

    df_amazon=(df_visual_l[(df_visual_l.platform=='amazon')]) 
    df_disney=(df_visual_l[(df_visual_l.platform=='disney')]) 
    df_hulu=(df_visual_l[(df_visual_l.platform=='hulu')]) 
    df_netflix=(df_visual_l[(df_visual_l.platform=='netflix')]) 

    df_amazon_categ=(df_amazon[df_amazon['category'].str.contains(genero,na=False)])
    df_disney_categ=(df_disney[df_disney['category'].str.contains(genero,na=False)])
    df_hulu_categ=(df_hulu[df_hulu['category'].str.contains(genero,na=False)])
    df_netflix_categ=(df_netflix[df_netflix['category'].str.contains(genero,na=False)])

    shape_a=df_amazon_categ.shape
    shape_a=shape_a[0]
    shape_d=df_disney_categ.shape
    shape_d=shape_d[0]
    shape_h=df_hulu_categ.shape
    shape_h=shape_h[0]
    shape_n=df_netflix_categ.shape
    shape_n=shape_n[0]

    lista=[shape_a,shape_d,shape_h,shape_n]
    mayor=(lista[0],0)
            
    for i,e in enumerate(lista):
        if e > mayor[0]:
            mayor=e,i

        else:
            mayor=mayor

        c=mayor[0]
        m=mayor[1]

        if m==0:
            p='Amazon'
        elif m==1:
            p='Disney'
        elif m==2:
            p='Hulu'
        elif m==3:
            p='Netflix'
    n=f'la plataforma que más repite el genero: {genero} es {p} por una cantidad de {c} veces '
    return n

#def get_actor
def get_actor(plataforma,anio):
    
    plataforma=str(plataforma.lower())
    anio=int(anio)
    df_visual_l['cast']=df_visual_l['cast'].fillna('null')

    df_plataforma=(df_visual_l[(df_visual_l.platform==plataforma)&(df_visual_l.release_year==anio)&(df_visual_l.cast!='null')])
    df_plataforma['cast']=df_plataforma['cast'].replace(' ,',',') 
    df_plataforma['cast']=df_plataforma['cast'].replace(', ',',') 

    lista_actores_unicos=[]

    for lista in df_plataforma['cast']:
        lista=str(lista).split(',')
        for actor in lista:
            actor=actor.strip()
            lista_actores_unicos.append(actor)
    lista_actores_unicos=list(set(lista_actores_unicos))

    lista_actores=[]
    lista_repetidos=[]
    dicc=dict()

    for lista in df_plataforma['cast']:
        lista=str(lista).split(',')
        for actor in lista:
            actor=actor.strip()
            lista_actores.append(actor)
    lista_actores_unicos=list(set(lista_actores))

    for i,e in enumerate(lista_actores):
        contador=lista_actores.count(e)
        dicc[e]=contador
    
    a=max(dicc, key=dicc.get)

    m=dicc.get(a)
    rta=f'el actor que más se repite es {a} en el año {anio} y la plataforma {plataforma}, y se repite {m} veces'
    return rta

    
