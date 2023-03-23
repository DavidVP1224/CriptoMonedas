"""En esta primera parte estamos importando y usando librerías necesarias para que el apache Airflow
    funcione con normalidad.
"""
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

"""Ahora importamos las librerías necesarias para que el código funcione perfectamente."""

import time
import requests
import json
import sqlite3 as sql
import datetime as dt

"""Definimos una función para ejecutar el código en el momento que el Airflow esté programado para ejecutar."""

def consulta_Monedas():
    
    """Definimos un STR con la URL de la API a la cual consumimos, luego le pasamos los parámetros a otra variable la cual definimos como 
        respuesta, con request hacemos la consulta dándole la URL y luego transformamos los datos que nos trajo en json para poder trabajar con ellos. 
    """
    
    api = "https://api.coingecko.com/api/v3/coins/"
    respuesta = requests.get(api)
    datos_coins = respuesta.json()
    
    """Creamos 3 listas, las cuales van a almacenar todos los datos que necesitamos de una misma moneda."""
    
    dicc_id = []
    dicc_datos = []
    dicc_fechas= []
    
    """Consultamos la fecha actual y la transformamos en Unix para poder pasarle el rango de busqueda a la siguiente consulta con la API."""

    fechaActual_unix = int(datetime.now().timestamp())
    id = 1
    """Creamos un ciclo for para recorrer todas y cada una de las monedas que existen en la API."""
    for cont in datos_coins:
        """Creamos una variable que va a estar en constante cambio dependiendo de si ya está guardada en nuestra base de datos, traemos el id que en este caso sería el mismo nombre de la moneda la cual vamos a consultarle
        el precio historico.
        """
        confirmacion_existe = False
        repetir_consulta = 1
        Coin_id = str(cont['id'])
        
        """Imprimos la moneda que estamos consultando y comenzamos a pasarle los parámetros a la URL, para luego hacer la consulta y repetir el preceso de transformar los datos consultados."""
        
        print(Coin_id)
        url_datos = f"https://api.coingecko.com/api/v3/coins/{Coin_id}/market_chart/range?vs_currency=usd&from=1515214800&to={fechaActual_unix}"
        respuesta_datos = requests.get(url_datos)
        datos = respuesta_datos.json()
        
        """Creamos el try exept que nos ayuda a definir lo que haga a continuación si la consulta con la API falla, o en este caso que tenga su limitante de no lograr consultar lo que le pedimos."""
        
        try:
            """En caso tal de que funcione perfectamente la consulta, tomará los datos de los prices(los precios de la moneda y la fecha a la que estuvo a ese valor)."""
            prices = datos["prices"]
            for n in prices:
                """Creamos un ciclo for y recorremos la lista para transformar los datos y guardarlos en las lista ya definidas anteriormente."""
                
                """Consultamos la fecha y la transformamos a STR para quitarle los últimos tres números, ya que vienen con tres ceros de más."""
                dato_fecha = str(n[0])
                dato_fecha = int(dato_fecha[:-3])
                
                """Transformamos la fecha de Unix a fecha normal y luego traemos el valor consultado en dolar y se lo damos a la variable (dato_valor_usd) como un STR para cargarlo de mejor forma en la base de datos."""
                
                dato_fecha = str(datetime.fromtimestamp(dato_fecha))
                dato_valor_usd = str(n[1])
                
                """Hacemos consulta con la base de datos local para validar si el dato actual ya está en la base de datos."""
                
                conn = sql.connect("/home/david/prueba/ejemplo-de-dag/BD/monedas.db")
                cursor = conn.cursor()
                instruc = f"SELECT fecha FROM ValorCoins WHERE Moneda = '{Coin_id}' AND fecha = '{dato_fecha}'"
                cursor.execute(instruc)
                datos_select_fecha = cursor.fetchall()
                
                try:
                    """Creamos el try para abarcar la posibilidad de que el dato consultado no exista en la base de datos."""
                    datos_select_fecha = datos_select_fecha[0][0]
                    
                    
                    """En caso tal de que el dato exista, el if va a omitir ese dato y va a editar la variable de confirmación para no guardar ese dato, de lo contrario va a guardar el dato en la lista para almacenarlo luego."""
                    if datos_select_fecha == dato_fecha:
                        confirmacion_existe = True
                    else:
                        """Guarda el dato en la lista."""
                        dicc_id.append(id)
                        dicc_datos.append(dato_valor_usd)
                        dicc_fechas.append(dato_fecha)
                        """Incrementa el id que va a guardar."""
                    id += 1
                except IndexError:
                    
                    """En caso tal de error de consulta de dato, se da por hecho que el dato no existe en la base de datos y lo guarda en la lista."""
                    confirmacion_existe = False
                    
                    dicc_id.append(id)
                    dicc_datos.append(dato_valor_usd)
                    dicc_fechas.append(dato_fecha)
                    id += 1
        except KeyError:
            """En caso de que ocurra el limitante de la API, se deberá esperar 88 segundos con el time.sleep antes de consultar."""
            
            time.sleep(88)
            url_datos = f"https://api.coingecko.com/api/v3/coins/{Coin_id}/market_chart/range?vs_currency=usd&from=1515214800&to={fechaActual_unix}"
            respuesta_datos = requests.get(url_datos)
            datos = respuesta_datos.json()
            prices = datos["prices"]
            
            """En caso de haber esperado ese tiempo, volverá a hacer lo mismo mensionado anteriormente."""
            
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
                    
        """Luego de guardar todos los datos no existentes consultados en las listas, continuamos con insertar los datos en la base de datos y crear la variable de conteo."""
        
        """Si en caso tal, hay datos inexistente, el if va a comprobarlo con la variable."""
        
        cont_insert = 0
        if confirmacion_existe == False:
            
            """El ciclo for va a repetirse el número de datos que hayan en la lista para insertarlos todos."""
            
            for p in dicc_id:
                print(cont_insert)
                conn = sql.connect("/home/david/prueba/ejemplo-de-dag/BD/monedas.db")
                cursor = conn.cursor()
                instruc = f"INSERT INTO ValorCoins VALUES ({p}, '{Coin_id}', '{dicc_datos[cont_insert]}', '{dicc_fechas[cont_insert]}')"
                cursor.execute(instruc)
                conn.commit()
                conn.close()
                cont_insert += 1
                
                """En caso de que ya exista todos los datos de esa moneda, va a imprimir que ya existe."""
        else:
            print(f"Ya existe {Coin_id}, {datos_select_fecha}")
        
        """Luego de terminar con los datos de una moneda, va a reiniciar las listas para continuar con la siguiente moneda."""
        
        dicc_id = []
        dicc_datos = []
        dicc_fechas= []

"""Estos son parámetros necesarios para el Airflow."""
        
default_args = {
    'owner': 'Davidvilla',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(seconds=5)
}

"""Estos son parámetros necesarios para el Airflow, descripción del DAG, le damos el tiempo de cada cuanto se va a ejecutar y la fecha de ejecución."""

dag = DAG(dag_id='Monedas_valor',
              description='Consulta el valor de las monedas desde el 2018 hasta hoy',
              default_args=default_args,
              start_date=datetime(2022, 5, 24, 6,00, 00), # Local hour
              # start_date=days_ago(2),
              schedule_interval='00 */24 * * *',
              catchup=False,
              concurrency=1,
              tags=['telefonia', 'dev']) 

"""Estos son parámetros necesarios para el Airflow, la tarea y lo que va a ejecutar cada ese tiempo que le pasamos, lo cual sería la función."""  

task_1 = PythonOperator(
    task_id='Monedas_virtuales',
    python_callable = consulta_Monedas,
    dag=dag,
)    
