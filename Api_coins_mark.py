from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

import psycopg2
import time
import requests
import datetime as dt

def ubdate():
    api = "https://api.coingecko.com/api/v3/coins/"
    respuesta = requests.get(api)
    datos_coins = respuesta.json()

    dicc_datos = []
    fechaActual_unix = int(datetime.now().timestamp())
    fecha = str(datetime.now())
    fecha = str(fecha[:-16])


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

    instruccion = f""" SELECT id FROM marcket_cap"""
    cursor.execute(instruccion)
    id_consulta = cursor.fetchall()
    id = id_consulta[-1][0]
    id = int(id + 1)

    for cont in datos_coins:
        confirmacion_existe = False
        Coin_id = str(cont['id'])
        print(Coin_id)
        
        url_datos = f"https://api.coingecko.com/api/v3/coins/{Coin_id}/market_chart/range?vs_currency=usd&from=1609477200&to={fechaActual_unix}"
        respuesta_datos = requests.get(url_datos)
        datos = respuesta_datos.json()
        
        try:
            Market = datos["market_caps"]
            valor_actual = str(datos["prices"][-1][-1])
            for n in Market:
                dato_valor_usd = n[1]
                
                dicc_datos.append(dato_valor_usd)
                
        except KeyError:
            time.sleep(120)
            
            url_datos = f"https://api.coingecko.com/api/v3/coins/{Coin_id}/market_chart/range?vs_currency=usd&from=1609477200&to={fechaActual_unix}"
            respuesta_datos = requests.get(url_datos)
            datos = respuesta_datos.json()
            
            Market = datos["market_caps"]
            valor_actual = str(datos["prices"][-1][-1])
            for n in Market:
                dato_valor_usd = n[1]
                
                dicc_datos.append(dato_valor_usd)
                
        cont_dicc = 0
        dato_anterior = dicc_datos[0]        
        for i in dicc_datos:
            dato_nuevo = i
            if cont_dicc != 0:
                dato_anterior += dato_nuevo
            cont_dicc += 1
        promedio = str(dato_anterior / cont_dicc)
        
        print(fecha)
        instruccion = f""" INSERT INTO marcket_cap VALUES ({id}, '{Coin_id}', '{promedio}', '{valor_actual}', '{fecha}' )"""
        cursor.execute(instruccion)
        connection.commit()
        id += 1
    connection.close()

default_args = {
    'owner': 'Davidvilla',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(seconds=5)
}

dag = DAG(dag_id='Monedas_valor_market',
              description='actualiza el market_cap de las monedas virtuales',
              default_args=default_args,
              start_date=datetime(2022, 5, 24, 6,00, 00), # Local hour
              # start_date=days_ago(2),
              schedule_interval='00 */24 * * *',
              catchup=False,
              concurrency=1,
              tags=['telefonia', 'dev']) 

task_1 = PythonOperator(
    task_id='Monedas_market',
    python_callable = ubdate,
    dag=dag,
)  