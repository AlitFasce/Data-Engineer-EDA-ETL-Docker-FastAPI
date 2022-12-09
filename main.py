from fastapi import FastAPI
import pandas as pd
from querys import *

app = FastAPI()


@app.get('/')
async def read_root():
    return {'API de Alit Fasce =) '}


@app.on_event('startup')
def startup():
    global df_visual_l
    df_visual_l=pd.read_csv("visualgeneral.csv")


@app.get("/get_max_duration/({anio},{plataforma},{min_o_season})")
async def query1(anio:int,plataforma:str,min_o_season:str):
    return get_max_duration(anio,plataforma,min_o_season)


@app.get("/get_count_plataform/{plataforma}")
async def query2(plataforma:str):
    return get_count_plataform(plataforma)

@app.get("/get_listedin/{genero}")
async def query3(genero:str):
    return get_listedin(genero)


@app.get("/get_actor/({plataforma},{anio})")
async def query4(plataforma:str,anio:int):
    return get_actor(plataforma,anio)

