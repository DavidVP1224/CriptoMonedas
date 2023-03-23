## Documentación Historia de las monedas en el mercado

## Requerimiento:
Historia de las principales monedas que hay en el mercado.

## Introducción:
Como bien sabemos el concepto de la moneda como medio de comercio sigue evolucionando.

Hoy en día, los comerciantes individuales buscan eludir la volatilidad y la imprevisibilidad de las monedas nacionales que estan vinculadas
a la toma de decisiones políticas por parte de los gobiernos, por ello han percibido con monedas digitales como el bitcoin que se negocian
completamente en entornos digitales.

Se dice que es muy poco probable que la moneda física tradicional desaparezca completamente ya que mostramos una necesidad de un medio físico
en el comercio, pero, al mismo tiempo, buscamos definiciones mas amplias del concepto de "moneda digital" para aumentar la eficiencia económica
y las ventajas obtenidas en el comercio.

A partir de esto, hacemos un análisis de las principales modenas digitales en el mercado y cómo esto ha tenido un impacto en su historia, haciendo
uso de herramientas como Airflow y Power BI para una predicción más certera. 

## Objetivos:
Comprender el desarrollo en las principales monedas haciendo comparación de un precio historico de hace cuatro años y un marketcap de hace dos años,
tratando de realizar un razonamiento lógico y dando a conocer su precio hasta el día de hoy. 

## Objetivos especificos:
Algunos objetivos especificos claves para el desarrollo del ejercicio son la consulta de los datos en la [API](www.coingecko.com "API"),
la base de datos PostgreSQL para guardar los datos, la vizualización y comparación con el Power BI.

## Alcance:
Consultar, extraer y transformar los datos requeridos de la API, aproximadamente una semana. Lograr crear, configurar y subir la información en la base de datos, aproximadamente media semana.
Lograr la visualización y presentación por medio de gráficas al finalizar la semana, en total, sin contar la documentación, se requieren dos semanas para terminar el proyecto.

## Ubuntu-Airflow:
Utilizamos una herramienta muy útil para orquestar el flujo de tareas, el cual se ejecutará cierto tiempo dependiendo de cuándo lo queramos o necesitemos. 
Los flujos de trabajo se extructuran en forma de (DAG) gráficos acíclicos dirigidos, esto permite la rapidez en repetir los flujos de trabajo.
Para instalarlo y utilizarlo en nuestra máquina, creamos un documento paso a paso de como hacerlo: [como instalar airflow](https://drive.google.com/file/d/1jL2FLIpyFKjVV5ueRrgey7YMYJmheZIK/view "como instalar airflow")

## Desarrollo de la Api:
Al entrar a la Api [documentación](www.coingecko.com/en/api/documentation "documentación") observamos a primera instancia la documentación para poder saber el procedimiento que debemos hacer al momento de desarrollar el código.
Debemos tener el cuenta que parte de la documentación nos sirve para poder darle solución a la solicitud asignada, en nuestro caso, debíamos convertir la
fecha en Unix ya que era una clave para obtener los datos que se requerían.
También, encontramos un limitante, había que esperar cierto tiempo después de un número de recargas en los datos, este problema lo logramos solucionar
con un tráfico de errores (time.sleep) que es un contador de espera para volver a consultar.

## Base de datos:
En el repositorio se encuentra una carpeta llamada BD en donde guardamos el precio historico de las monedas desde el 01/01/2018 hasta el 16/03/2023.

## Power BI Desktop:
Ahora, en Power BI se creará los gráficos aplicándole diferentes filtros para conocer el top 10 de criptomonedas con mayor marketcap, el precio historico, predicción de los próximos días y, además, añadirle un banner de diseño acorde a lo planteado.

Primero, se importará la base de datos de la siguiente manera:

Seleccionamos "Obtener datos":
[imagen 1](https://drive.google.com/file/d/1FvW_rIhKLq1MYvuBUc66TRZ1YvWs7BuJ/view "imagen 1")

Luego en "Más...":
[imagen 2](https://drive.google.com/file/d/10NJIkG1s1hp1o9wkdq2wwwBdXxWdCcXP/view "imagen 2")

Buscaremos "Base de datos PostgresSQL", la seleccionamos y luego la conectamos:
[imagen 3](https://drive.google.com/file/d/1aNGTh2v2pLcXZK-Ddis1VVwoLpODgsGM/view "imagen 3")

Ahora se ingresa el servidor localhost o 127.0.0.1 y el nombre de la base de datos y aceptamos:
[imagen 4](https://drive.google.com/file/d/13JTgmHlhCD239SVGVNx-R0mseNr9igwS/view "imagen 4")

Es probable que al intentar importar la base de datos aparezca el siguiente error:
[imagen 5](https://drive.google.com/file/d/1swVO-icgNXkYjzIbfM6oMuFJ4Y21pk89/view "imagen 5")

Para solucionarlo habrá que descargar e instalar la extención NPGSQL mediante el siguiente link: [enlace](https://github.com/npgsql/Npgsql/releases/tag/v2.2.4.3 "enlace")

Al ingresar al link aparecerán 9 archivos, preferiblemente se elegirá uno de los que estan señalados en la siguiente imagen:
[imagen 6](https://drive.google.com/file/d/1F76URzPXwFAM17r24HGZWORUKPiRLUTf/view "imagen 6")

Cuando se descargue procederemos a ejecutar el setup:
[imagen 7](https://drive.google.com/file/d/1PXUt2Ew9XL4UVm3L0bANFKHvbnjY3fRh/view "imagen 7")
[imagen 8](https://drive.google.com/file/d/1bFrNHAYrLoDYlzS9qSJnsNEU2jNSsyvZ/view "imagen 8")

Ahora instalaremos la extención, a continuación daremos en "I Agree":
[imagen 9](https://drive.google.com/file/d/1_9NPAKdkcYIDPrBYpTn6x-8i_JOFsB3p/view "imagen 9")

Después dejamos seleccionados todos los componestes y presionamos en "Next":
[imagen 10](https://drive.google.com/file/d/1nREjisBnVyX1miUmndvgOZIsTO_d2dCZ/view "imagen 10")

Por último lo instalaremos:
[imagen 11](https://drive.google.com/file/d/12hXii1zYB4_6DuCxGePprwAyH1DRy36L/view "imagen 11")

Luego de instalarlo habrá que cerrar el Power BI y seguir los pasos iniciales nuevamente y se debería de importar correctamente la base de datos.

## Banner:
Ahora en Power Point se creará un diseño (banner) acorde a la API (criptomonedas):
[imagen 12](https://drive.google.com/file/d/1piEQOupFD6aY18y0s8tijAe1ZRxIoKX1/view "imagen 12")

Después procederemos a guardar el banner, daremos en Archivo:
[imagen 13](https://drive.google.com/file/d/1NA6aaYy1aYbbpcxNU8jMeKcAsJ16_aEQ/view "imagen 13")

Guardar como y Examinar:
[imagen 14](https://drive.google.com/file/d/1ZJg5FrkCxEH4JmFZuGtk5qa0n5rYdGiR/view "imagen 14")

Ahora, en el apartado "Tipo", cambiaremos el formato del banner a JPEG o PNG, para luego importarlo a Power BI con más facilidad:
[imagen 15](https://drive.google.com/file/d/1OMKqH6PwITwL3lrRiGodkBs571BM83FK/view "imagen 15")

## Importar banner a Power BI
Para importar el banner nos iremos al apartado de "Visualizaciones" y luego en "Dar formato" a la página del informe (el símbolo de una hoja de papel y un pincel):
[imagen 16](https://drive.google.com/file/d/1btnHZrO9hwmozGGArhTtrYCYds2IY191/view "imagen 16")

Seleccionamos "Fondo del lienzo" y luego en "Examinar...":
[imagen 17](https://drive.google.com/file/d/1bL83xUYBJVmWialktegoG0_FxHTQR1W8/view "imagen 17")

Buscamos el banner anteriormente creado y lo abrimos:
[imagen 18](https://drive.google.com/file/d/1maCmItsGSoy0I0UIr8Z33bOeAex6TlUj/view "imagen 18")

Luego de importarlo en primera instancia no aparecerá el banner, para esto se tendría que reducir la transparencia a 0%:
[imagen 19](https://drive.google.com/file/d/1s1LP78-B_Uz4Lk8mSmnVJxVfsmHIAev5/view "imagen 19")

Para ajustar un poco la imagen y que quede simétrica con la página del Power BI, nos iremos a "Ajuste de imagen" y seleccionamos "Ajustar":
[imagen 20](https://drive.google.com/file/d/1tTFcnut7oMQxgX6czsj26xqCHZcV4nHl/view "imagen 20")

Mediante este link se podrán ver las gráficas realizadas en el Power BI:
[enlace](https://app.powerbi.com/links/r24R0VlwJ-?ctid=650039fd-712a-4fe1-b863-86103c425c17&pbi_source=linkShare "enlace")

## Limitantes y soluciones:
- Primer limitante: la API cuenta con un límite de solicitudes en un determinado tiempo.
- Solución: tuvimos en cuenta un tiempo de espera antes de realizar la misma consulta cuando esta generaba error.
- Segundo limitante: la base de datos, ya que estabamos utilizando una base de datos local en una carpeta y no era lo más recomendado.
- Solución: usar PostgreSQL dentro del Ubuntu para almacenar la base de datos.
- Tercera limitante: la lectura de base de datos entre el Power BI y los puertos del PostgreSQL.
- Solución: descargamos el NPGSQL para que Power BI reconociera la conexión.

## Conclución:
Logramos consultar los datos que se requerían, esto lo hicimos facilmente consultando la documentación de la API, luego logramos extraer y transformar esta información para subir a la base de datos y se pudimos visualizar por medio de gráficos comparativos en Power BI.
