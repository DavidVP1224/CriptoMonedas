"""En esta primera parte estamos importando y usando librerias necesarias para que el apache airflow
    funcione con normalidad
"""

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

"""Ahora importamos las librerias necesarias para que el codigo funcione perfectamente"""
"""Usamos psycopg2 para la coneccion con la base de datos"""

import psycopg2
import time
import requests
import datetime as dt

"""Definimos una funcion para ejecutar el codigo en el momento que el airflow esté programado para ejecutar"""

def ubdate():
    
    """Definimos un str con la url de la api a la cual consumimos, luego le pasamos los parametros a otra variable la cual definimos como 
        respuesta, con request hacemos la consulta dandole la url y luego transformamos los datos que nos trajo en json para poder trabajar con ellos 
    """
    
    api = "https://api.coingecko.com/api/v3/coins/"
    respuesta = requests.get(api)
    datos_coins = respuesta.json()
    
    """Definimos una lista para almacenar los datos que vamos a guardar en la base de datos, y luego definimos la fecha actual como unix y la fecha actual como9 str para quitarle la hora
        ya que no la necesitamos
    """

    dicc_datos = []
    fechaActual_unix = int(datetime.now().timestamp())
    fecha = str(datetime.now())
    fecha = str(fecha[:-16])
    
    """Creamos un try para hacer la conexion con la base de datos, y si falla poder saber el porque"""

    try:
        connection = psycopg2.connect(
            host='localhost',
            user='david',
            password='david0506',
            database='db_trabajos'
        )
        cursor = connection.cursor()
    except Exception as ex:
        print(ex)
        print("No se pudo conectar a la base de datos")
        
    """Luego consultamos el ultimo id de la base de datos para sumarlo y llevar el orden"""

    instruccion = f""" SELECT id FROM marcket_cap"""
    cursor.execute(instruccion)
    id_consulta = cursor.fetchall()
    id = id_consulta[-1][0]
    id = int(id + 1)
    
    """Creamos un ciclo for para recorrer la lista de monedas existentes, sacamos el id que vendria siendo el nombre de la moneda y lo imprimimos"""

    for cont in datos_coins:
        confirmacion_existe = False
        Coin_id = str(cont['id'])
        print(Coin_id)
        
        """Con los datos que ya tenemos, consultamos los datos de este mismo año hasta la fecha actual de las monedas, lo transformamos en json y guardamos en una variable"""
        
        url_datos = f"https://api.coingecko.com/api/v3/coins/{Coin_id}/market_chart/range?vs_currency=usd&from=1609477200&to={fechaActual_unix}"
        respuesta_datos = requests.get(url_datos)
        datos = respuesta_datos.json()
        
        """Ceramos el try except por si la consulta falla con el limitante de la api"""
        
        try:
            
            """Sacamos los datros del market cap y los almacenamos en una variable, la cual comenzamos a extraer con un ciclo for que la recorra y lo almacenamos en la lista"""
            Market = datos["market_caps"]
            valor_actual = str(datos["prices"][-1][-1])
            for n in Market:
                dato_valor_usd = n[1]
                
                dicc_datos.append(dato_valor_usd)
                
        except KeyError:
            
            """En caso tal de que la consulta falle por el limitante de la api, va a dar un tiempo de espera de 2 minutos antes de volver a consultar la misma moneda en la que se habia quedado"""
            
            time.sleep(120)
            
            url_datos = f"https://api.coingecko.com/api/v3/coins/{Coin_id}/market_chart/range?vs_currency=usd&from=1609477200&to={fechaActual_unix}"
            respuesta_datos = requests.get(url_datos)
            datos = respuesta_datos.json()
            
            """Con los datos que ya tenemos, consultamos los datos de este mismo año hasta la fecha actual de las monedas, lo transformamos en json y guardamos en una variable"""
            
            """Sacamos los datros del market cap y los almacenamos en una variable, la cual comenzamos a extraer con un ciclo for que la recorra y lo almacenamos en la lista"""
            Market = datos["market_caps"]
            valor_actual = str(datos["prices"][-1][-1])
            for n in Market:
                dato_valor_usd = n[1]
                
                dicc_datos.append(dato_valor_usd)
                
        """Luego de tener todos los datos del market cap de una misma moneda almacenados en la lista, procedemos a crear un ciclo for para sacarle el promedio"""
        
        cont_dicc = 0
        dato_anterior = dicc_datos[0]        
        for i in dicc_datos:
            dato_nuevo = i
            if cont_dicc != 0:
                dato_anterior += dato_nuevo
            cont_dicc += 1
        promedio = str(dato_anterior / cont_dicc)
        
        """Insertamos los datos tal cual los extrajimos y transformamos, junto con la fecha a la que de tomó los datos, incrementamos el id para seguir con la siguiente moneda y al finalizar todo cerramos la base de datos"""
        
        instruccion = f""" INSERT INTO marcket_cap VALUES ({id}, '{Coin_id}', '{promedio}', '{valor_actual}', '{fecha}' )"""
        cursor.execute(instruccion)
        connection.commit()
        id += 1
    connection.close()
    
    
    """Estos son parametros necesarios para el airflow"""

default_args = {
    'owner': 'Davidvilla',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(seconds=5)
}

"""Estos son parametros necesarios para el airflow, descripcion del dag, le damos el tiempo de cada cuanto se va a ejecutar y la fecha de ejecucion"""


dag = DAG(dag_id='Monedas_valor_market',
              description='actualiza el market_cap de las monedas virtuales',
              default_args=default_args,
              start_date=datetime(2022, 5, 24, 6,00, 00), # Local hour
              # start_date=days_ago(2),
              schedule_interval='00 */24 * * *',
              catchup=False,
              concurrency=1,
              tags=['telefonia', 'dev']) 


"""Estos son parametros necesarios para el airflow, la tarea y lo que va a ejecutar cada ese tiempo que le pasamos, lo cual seria la funsion"""  


task_1 = PythonOperator(
    task_id='Monedas_market',
    python_callable = ubdate,
    dag=dag,
)  