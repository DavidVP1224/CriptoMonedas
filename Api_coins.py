from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

import time
import requests
import json
import sqlite3 as sql
import datetime as dt

def consulta_Monedas():
    api = "https://api.coingecko.com/api/v3/coins/"
    respuesta = requests.get(api)
    datos_coins = respuesta.json()

    dicc_id = []
    dicc_datos = []
    dicc_fechas= []

    fechaActual_unix = int(datetime.now().timestamp())
    id = 1
    for cont in datos_coins:
        confirmacion_existe = False
        repetir_consulta = 1
        Coin_id = str(cont['id'])

        print(Coin_id)
        url_datos = f"https://api.coingecko.com/api/v3/coins/{Coin_id}/market_chart/range?vs_currency=usd&from=1515214800&to={fechaActual_unix}"
        respuesta_datos = requests.get(url_datos)
        datos = respuesta_datos.json()
        
        try:
            prices = datos["prices"]
            for n in prices:
                dato_fecha = str(n[0])
                dato_fecha = int(dato_fecha[:-3])
                
                dato_fecha = str(datetime.fromtimestamp(dato_fecha))
                dato_valor_usd = str(n[1])
                
                conn = sql.connect("/home/david/prueba/ejemplo-de-dag/BD/monedas.db")
                cursor = conn.cursor()
                instruc = f"SELECT fecha FROM ValorCoins WHERE Moneda = '{Coin_id}' AND fecha = '{dato_fecha}'"
                cursor.execute(instruc)
                datos_select_fecha = cursor.fetchall()
                
                try:
                    datos_select_fecha = datos_select_fecha[0][0]
                    
                    if datos_select_fecha == dato_fecha:
                        confirmacion_existe = True
                    else:
                        dicc_id.append(id)
                        dicc_datos.append(dato_valor_usd)
                        dicc_fechas.append(dato_fecha)
                    id += 1
                except IndexError:
                    confirmacion_existe = False
                    
                    dicc_id.append(id)
                    dicc_datos.append(dato_valor_usd)
                    dicc_fechas.append(dato_fecha)
                    id += 1
        except KeyError:
            time.sleep(88)
            url_datos = f"https://api.coingecko.com/api/v3/coins/{Coin_id}/market_chart/range?vs_currency=usd&from=1515214800&to=1677860760"
            respuesta_datos = requests.get(url_datos)
            datos = respuesta_datos.json()
            prices = datos["prices"]
            
            for n in prices:
                dato_fecha = str(n[0])
                dato_fecha = int(dato_fecha[:-3])
                
                dato_fecha = str(datetime.fromtimestamp(dato_fecha))
                dato_valor_usd = str(n[1])
                
                conn = sql.connect("/home/david/prueba/ejemplo-de-dag/BD/monedas.db")
                cursor = conn.cursor()
                instruc = f"SELECT fecha FROM ValorCoins WHERE Moneda = '{Coin_id}' AND fecha = '{dato_fecha}'"
                cursor.execute(instruc)
                datos_select_fecha = cursor.fetchall()
                
                try:
                    datos_select_fecha = datos_select_fecha[0][0]
                    
                    if datos_select_fecha == dato_fecha:
                        confirmacion_existe = True
                    else:
                        dicc_id.append(id)
                        dicc_datos.append(dato_valor_usd)
                        dicc_fechas.append(dato_fecha)
                    id += 1
                except IndexError:
                    confirmacion_existe = False
                    
                    dicc_id.append(id)
                    dicc_datos.append(dato_valor_usd)
                    dicc_fechas.append(dato_fecha)
                    id += 1
        cont_insert = 0
        if confirmacion_existe == False:
            
            for p in dicc_id:
                print(cont_insert)
                conn = sql.connect("/home/david/prueba/ejemplo-de-dag/BD/monedas.db")
                cursor = conn.cursor()
                instruc = f"INSERT INTO ValorCoins VALUES ({p}, '{Coin_id}', '{dicc_datos[cont_insert]}', '{dicc_fechas[cont_insert]}')"
                cursor.execute(instruc)
                conn.commit()
                conn.close()
                cont_insert += 1
        else:
            print(f"ya existe {Coin_id}, {datos_select_fecha}")
        dicc_id = []
        dicc_datos = []
        dicc_fechas= []

        
default_args = {
    'owner': 'Davidvilla',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(seconds=5)
}

dag = DAG(dag_id='Monedas_valor',
              description='Consulta el valor de las monedas desde el 2018 hasta hoy',
              default_args=default_args,
              start_date=datetime(2022, 5, 24, 6,00, 00), # Local hour
              # start_date=days_ago(2),
              schedule_interval='00 */24 * * *',
              catchup=False,
              concurrency=1,
              tags=['telefonia', 'dev'])   

task_1 = PythonOperator(
    task_id='Monedas_virtuales',
    python_callable = consulta_Monedas,
    dag=dag,
)    
