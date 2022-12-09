#librerias a importar_las mismas tambien estan en el archivo requierments del docker
import pandas as pd
import numpy as np



#funcion para abrir achivos
'''
def abriendo_archivos(path):
    with open (path,'rb') as f:        
        tipoencoding=chardet.detect(f.read())

        if pl(path).suffix == ".csv":
           df= pd.read_csv(path,encoding=tipoencoding["encoding"], sep=None, engine="python",decimal=".")

        if pl(path).suffix==".json"or pl(path).suffix==".js":
            df=pd.read_json(path, precise_float=True)
    
    return df
    '''

#df_visual_l=pd.read_csv("visualgeneral.csv")


# para elimnar columnas que NO voy a necesitar en este proyecto_ ver criterio y readme
def eliminando_columnas(df):
    df.drop(columns=['director'], inplace = True)
    df.drop(columns=['country'], inplace = True)
    df.drop(columns=['date_added'], inplace = True)
    df.drop(columns=['rating'], inplace = True)
    df.drop(columns=['description'], inplace = True)
    return df

# para separar la columna duracion entre temporadas y duracion de las películas
def separando_duration(df):
    df['duration'].fillna('0 min', inplace=True)
    lista_season=[]
    lista_dur_time=[]

    for i in df['duration']: 
        i=str(i)
        m=str(i.split(" ",1)[1])
        n=int(i.split(" ",1)[0])
        
    
        if m=='min':
            lista_dur_time.append(n)
            lista_season.append(0)
        elif m=='Season' or m=='Seasons': 
            lista_season.append(n) 
            lista_dur_time.append(0)

    s_season=pd.Series(lista_season)
    s_dur_time=pd.Series(lista_dur_time)
    df['seasson_quantity']= s_season
    df['movie_duration']= s_dur_time
    #df(columns=['duration'], inplace = True)
    return df

#para despejar la cabeza de fastAPI, me puse a hacer improvement del hardcodeo

def separando_duration02(df):
    df['movie_duration']=df['duration'].apply( lambda i: i.split()[0] if i.split()[1]=='min' else '0')
    df['seasson_quantity']=df['duration'].apply( lambda i: i.split()[0] if i.split(" ",1)[1]=='Seassons' or i.split(" ",1)[1]=='Season' else '0')
    return df

#para definir un nuevo id contemplando los anteriores para darle trazabilidad al dato

def nuevo_id(df, col_input,letra):
    serie=list(df[col_input])
    #serie=(serie)
    nueva_col=[]
    
    for i in serie:
        m=''.join(i+letra)
        nueva_col.append(m)

    nueva_col=np.array(nueva_col)
    nueva_col.reshape(1,-1)
    df['ID_new']=nueva_col
    return df

#para hacer una lista devalores unicos    
def lista_datos_unicos(df,columna):
    lista_aux1=[]
    for i in df[columna]:
        m=i.split(",")
        for i in m:
            lista_aux1.append(i)
    lista_categorias=set(lista_aux1)   
    n=len(lista_categorias)

    return n, lista_categorias

