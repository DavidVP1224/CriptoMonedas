##Docuementacion Codigo Historia de las monedas en el mercado

##Requrimiento
Historia de las de las principales monedas que hay en el mercado

##Introduccion
Como bien sabemos el concepto de la moneda como medio de comercio y ahora digital sigue evolucionando.

Hoy en dia los comerciantes individuales buscan eludir la volatilidad y la imprevisibilidad de las monedas nacionales que estan vinculadas
a la toma de decisiones politicas por parte de los gobiernos, por ello han percibido con monedas digitales como el bitcoin que se negocian
completamente en eterno electronicos en linea.

Se dice que es muy poco probable que la moneda fisica tradicional desaparezca completamente ya que mostramos una necesidad de un medio fisico
en el comercio, pero al mismo tiempo buscamos definiciones mas amplias del concepto de "moneda digital" para aumentar la eficiencia economica
y las ventajas obtenidas en el comercio.

A partir de esto hacemos un analisis de las principales modenas digitales en el mercado y como esto a tenido un impacto en su historia, haciendo
uso de principales herramientas como Airflow y power bi para su mas certera prediccion. 

##Objetivos
Comprender el desarrollo en las principales monedas haciendo comparacion de un precio historico de hace cuatro años y un marketcap de hace dos años.
tratando de realizar un razonamiento logico y dando conocer su precio hasta el dia de hoy. 

##Objetivos especificos:
Algunos objetivos especificos claves para el desarrollo del ejercicio son la consulta de los datos en la [API](www.coingecko.com "API"),
la base de datos PostgreSQL para guardar los datos, la vizualizacion y comparacion con el Powerbi.

##Alcance:
Consuntar, extraer y transformar los datos requeridos de la API aproximadamente una semana. Lograr crear, configurar y subir los datos en la base de datos aproximadamente media semana.
Lograr la visualizacion y presentacion por medio de graficas al finalizar la semana, En total sin contar la documentacion es requerido dos semanas para terminar el proyecto.

##Ubuntu-Airflow
Utilizamos una herramienta muy util para orquestar el flujo de tareas el cual se ejecutara cierto tiempo dependiendo de cuando lo queramos o necesitemos. 
Los flujos de trabajo se extructuran en forma de (DAG) graficos aciclicos dirigidos, lo cual representa una tarea especifica con nodos cada uno de ellos,
esto permite la rapidez en repetir los flujos de trabajo.
Para instalarlo y utilizarlo en nuestra maquina creamos un documento paso a paso de como hacerlo: [como instalar airflow](https://drive.google.com/file/d/1jL2FLIpyFKjVV5ueRrgey7YMYJmheZIK/view "como instalar airflow")

##Desarrollo de la Api
Al entrar a la Api [documentación](www.coingecko.com/en/api/documentation "documentación") observamos a primera instancia la documentacion para poder saber el procedimiento que debemos
tener al momento de desarrollar el codigo.
Debemos tener el cuenta que parte de la documentacion nos sirve para poder darle solucion a la solicitud asignada, en nuestro caso debiamos convertir la
fecha en Unix ya que era una clave para obtener los datos que necesitabamos.
Tambien encontramos un limitante la cual habia que esperar cierto tiempo despues de un numero de recarga en los datos, este problema lo logramos solucionar
con un trafico de errores (time.sleep) que es un contador de espera para volver a consultar.

##Base de datos
En el repositorio se encuentra una carpeta llamada BD en donde guardamos el precio historico de las monedas desde el 2018 hasta el 16/03/2023

##Power BI Desktop
Ahora en power bi se creara los graficos aplicandole diferentes filtros para conocer el top 10 de criptomonedas con mayor marketcap, el precio historico, prediccion de los proximos dias y ademas de añadirle un banner de diseño acorde a lo planteado.

primero se realizara importar la base de datos de la siguiente manera:

seleccionamos obtener datos:
[imagen 1](https://drive.google.com/file/d/1FvW_rIhKLq1MYvuBUc66TRZ1YvWs7BuJ/view "imagen 1")

luego en mas:
[imagen 2](https://drive.google.com/file/d/10NJIkG1s1hp1o9wkdq2wwwBdXxWdCcXP/view "imagen 2")

buscaremos base de datos postgresSQL, la seleccionamos y luego en conectar:
[imagen 3](https://drive.google.com/file/d/1aNGTh2v2pLcXZK-Ddis1VVwoLpODgsGM/view "imagen 3")

ahora se ingresa el servidor localhost o 127.0.0.1 y el nombre de la base de datos, luego en aceptar:
[imagen 4](https://drive.google.com/file/d/13JTgmHlhCD239SVGVNx-R0mseNr9igwS/view "imagen 4")

es probable que al intentar importar la base de datos aparesca el siguiente error:
[imagen 5](https://drive.google.com/file/d/1swVO-icgNXkYjzIbfM6oMuFJ4Y21pk89/view "imagen 5")

para solucionarlo habra que descargar e instalar la extencion NPGSQL mediante el siguiente link: [enlace](https://github.com/npgsql/Npgsql/releases/tag/v2.2.4.3 "enlace")

al ingresar al link apareceran 9 archivos, preferiblemente se elegira uno de los que estan señalados:
[imagen 6](https://drive.google.com/file/d/1F76URzPXwFAM17r24HGZWORUKPiRLUTf/view "imagen 6")

cuando se descargue procederemos a ejecutar el setup:
[imagen 7](https://drive.google.com/file/d/1PXUt2Ew9XL4UVm3L0bANFKHvbnjY3fRh/view "imagen 7")
[imagen 8](https://drive.google.com/file/d/1bFrNHAYrLoDYlzS9qSJnsNEU2jNSsyvZ/view "imagen 8")

ahora instalaremos la extencion, a continuacion daremos en i agree:
[imagen 9](https://drive.google.com/file/d/1_9NPAKdkcYIDPrBYpTn6x-8i_JOFsB3p/view "imagen 9")

despues dejamos seleccionados todos los componestes y damos en next:
[imagen 10](https://drive.google.com/file/d/1nREjisBnVyX1miUmndvgOZIsTO_d2dCZ/view "imagen 10")

por ultimo daremos en instalar:
[imagen 11](https://drive.google.com/file/d/12hXii1zYB4_6DuCxGePprwAyH1DRy36L/view "imagen 11")

luego de instalarlo habra que cerrar el power bi y seguir los pasos iniciales nuevamente y ya deberia de importar correctamente.

##Banner
ahora en power point se creara un diseño (banner) acorde a la API (criptomonedas):
[imagen 12](https://drive.google.com/file/d/1piEQOupFD6aY18y0s8tijAe1ZRxIoKX1/view "imagen 12")

despues procederemos a guardar el banner, daremos en archivo:
[imagen 13](https://drive.google.com/file/d/1NA6aaYy1aYbbpcxNU8jMeKcAsJ16_aEQ/view "imagen 13")

guardar como y examinar:
[imagen 14](https://drive.google.com/file/d/1ZJg5FrkCxEH4JmFZuGtk5qa0n5rYdGiR/view "imagen 14")

ahora daremos en el apartado tipo y cambiaremos el formato del banner a jpeg o png, para luego importarlo a power bi con mas facilidad:
[imagen 15](https://drive.google.com/file/d/1OMKqH6PwITwL3lrRiGodkBs571BM83FK/view "imagen 15")

##Importar banner a power BI
para importar el banner no iremos al apartado de visualización y luego en dar formato a la pagina del informe (el simbolo de una hoja de papel y un pincel):
[imagen 16](https://drive.google.com/file/d/1btnHZrO9hwmozGGArhTtrYCYds2IY191/view "imagen 16")

seleccionamos fondo del lienzo y luego en examinar:
[imagen 17](https://drive.google.com/file/d/1bL83xUYBJVmWialktegoG0_FxHTQR1W8/view "imagen 17")

buscamos el banner anteriormente creado y lo abrimos:
[imagen 18](https://drive.google.com/file/d/1maCmItsGSoy0I0UIr8Z33bOeAex6TlUj/view "imagen 18")

luego de importarlo en primera instancia no aparecera el banner, para esto se tendria que reducir la transparencia a 0%:
[imagen 19](https://drive.google.com/file/d/1s1LP78-B_Uz4Lk8mSmnVJxVfsmHIAev5/view "imagen 19")

para ajustar un poco la imagen y que quede simetrica con la pagina del power bi, nos iremos a ajuste de imagen y seleccionamos ajustar:
[imagen 20](https://drive.google.com/file/d/1tTFcnut7oMQxgX6czsj26xqCHZcV4nHl/view "imagen 20")

mediante este link se podran ver las graficas realizadas en el power bi:
[enlace](https://app.powerbi.com/links/r24R0VlwJ-?ctid=650039fd-712a-4fe1-b863-86103c425c17&pbi_source=linkShare "enlace")

##Limitantes y soluciones:
- Primer limitante: la API cuenta con un limite de solicitudes en un determinado tiempo.
- Solucion: tuvimos en cuenta un tiempo de espera antes de realizar la misma consulta cuando esta generaba error.
- Segundo limitante: la base de datos ya que estabamos utilizando una base de datos local en una carpeta y no era lo mas recomendado.
- Solucion: usar PostgreSQL dentro del Ubuntu para almacenar la base de datos.
- Tercera liminate: la lectura de base de datos entre el Power bi y los puertos del PostgreSQL.
- Solucion: descargamos el NPGSQL para que Power bi reconociera la conexion.

##Conclucion:
Logramos consultar los datos que se requerian, esto lo hicimos facilmente viendo la documentacion de la API, luego logramos extraer y transformar estos datos
para subir a la base de datos y se pudo visualizar por medio de graficos comparativos en Powerbi.
