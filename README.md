Data-Engineer-EDA-ETL-Docker-FastAPI

_ PROYECTO INDIVIDUAL Nº1 para Henry_ Diciembre 2022 _ Data Engineering

Este es un proyecto trabaja sobre archivos en csv y json, luego se hace un  EDA  y ETL (solo a los fines de este proyecto), para luego levantarlo con docker en una API hecha por fastAPI

![imagen](https://www.careerguide.com/career/wp-content/uploads/2020/03/Floating-head-for-GIF-1.gif.gif)


## **Introducción**

Soy Alit Fasce, en esta oportunidad estoy realizando este proyecto, como parte de los laboratorios de Henry donde he realizado un Bootcamp de 6 módulos, intensivos. 

Puedes ver el [Programa Data Science - Henry](https://www.soyhenry.com/carrera-data-science)

## **Objetivo de trabajo**


El proyecto consiste en realizar una ingesta de datos desde diversas fuentes, posteriormente aplicar las transformaciones que consideren pertinentes, y luego disponibilizar los datos limpios para su consulta a través de una API. Esta API deberán construirla en un entorno virtual dockerizado.

Los datos serán provistos en archivos de diferentes extensiones, como *csv* o *json*. Se espera que realicen un EDA para cada dataset y corrijan los tipos de datos, valores nulos y duplicados, entre otras tareas. Posteriormente, tendrán que relacionar los datasets así pueden acceder a su información por medio de consultas a la API.

Las consultas a realizar son:

+ Máxima duración según tipo de film (película/serie), por plataforma y por año:

    El request debe ser: get_max_duration(año, plataforma, [min o season])

+ Cantidad de películas y series (separado) por plataforma

    El request debe ser: get_count_plataform(plataforma)  
  
+ Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.

    El request debe ser: get_listedin('genero')  

    Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.

+ Actor que más se repite según plataforma y año.

  El request debe ser: get_actor(plataforma, año)
[Consigna completa del PI](https://github.com/HX-FAshur/PI01_DATA05)

## *Trabajo realizado y Criterio**

- Se realizó el trabajo de EDA, considerando el objetivo planteado se analizaron los faltantes y defector en la estructura de los datasets provistos considerando los datos a ser utilizados para realizar las querys finales, se obtuvo un informe. 

- El trabajo de ETL, especialmente la limpieza, se con foco en el objetivo propuesto.

 Dado que las querys propuestas requieren, UNICAMENTE de las columnas: 

        - title
        - type
        - cast
        - listed_in (categoria)
        - release year 
        - platform
        - duration

Se eliminaron todas las demás columnas, ya que no tenía sentido limpiarlas, estandarizar formato y normalizarlas con id porque, el objetivo de este proyecto es hacer la conexión con FastAPI, levantarla en un Docker y hacer las 4 consultas pleanteadas. 

El objetivo NO es realizar un datawarehouse estructurado donde podamos realizar cualquier consulta, por lo que el ELT hubiera sido completamente distinto con un criterio de conservar y completar todo dato faltante en todas las columnas y generar estructuras posiblemente de estrella con tablas de dimensiones nuevas con id de películas, actores y plataformas; que referencien a una tabla central de hecho. 


## **Estructura de Carpetas**

- Datasets
        - archivos raw
- EDA
        -  archivo jupiter Notebook (con anotaciones en markdown de los pasos realizados) 
        -  EDA Report txt
- ETL
        - archivo jupiter Notebook (con anotaciones en markdown de los pasos realizados)
	    - archivo funciones.py

- csv_limpios
        - visualglobal.csv (archivo generado luego de la limpieza en pandas)


 Archivos globales: 

-	querys.py (donde se llamar al archivo limpio y están las consultas en forma de funciones)
-	main.py (estructura de API)
-	dockerfile
-	requierments.txt (para traer el al contenedor todas las herramientas que utilizamos en los demás archivos)

## **Herramientas utilizadas:**

        - Python
        - Pandas
        - Numpy
        - Docker
        - FastAPI

## **Material consultado**

- + https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi/ 

- + https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker

- + https://fastapi.tiangolo.com/tutorial/

- + https://www.youtube.com/watch?v=tLKKmouUams&t=745s

- + https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html

- + https://naps.com.mx/blog/uso-de-query-con-pandas-en-python/

- + https://joserzapata.github.io/courses/python-ciencia-datos/pandas/
