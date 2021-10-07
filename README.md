# <img src="assets/start.png" width="50" height="50"/> DailyMaze

#### Descripción
DailyMaze es una aplicación que genera un laberinto según la configuración del usuario y lo publica en la cuenta de
Twitter configurada.

#### Configuración
Para usar el programa primero se debe copiar el fichero config-example.yaml y llamarlo config.yaml. Ahora podemos
personalizar el laberinto según las opciones dadas:
- **height**: Altura en celdas del laberinto.
- **width**: Ancho en celdas del laberinto.
- **cell_size**: Tamaño en píxels de cada celda.
- **credits**: Nombre de la cuenta u otro pequeño texto para mostrar debajo del laberinto.
- **twitter**: Aquí se introducen las api key de Twitter.
- **messages**: Mensajes personalizables para cada día de la semana que se publicarán junto al laberinto.

#### Uso de la aplicación
Se debe pasar el parámetro `--time` seguido de `morning` o `evening`. Es decir: 

- `python main.py --time morning` para la ejecución por la mañana.

- `python main.py --time evening` para la ejecución por la noche.

Es posible la ejecución sin el párametro --time, pero en este caso tan solo se publicaría la imagen sin mensaje alguno.

#### Automatizar ejecución
Una forma de automatizar la publicación de laberintos sería mediante la creación de un fichero .bat, del cual se tiene 
un ejemplo junto al código, y el uso del Programador de tareas de Windows. Tan solo habría que configurar la hora de 
ejecución, que se ejecute en la misma carpeta del script y pasar como argumento `morning` o `evening`, según la hora 
programada. El .bat se encarga de ejecutar el script de Python y pasar los argumentos necesarios.

#### Stack utilizado
Para el desarrollo se ha utilzado Python 3.9, junto a las siguientes librerías:
- Pillow: Para la generación de la imagen del laberinto.
- PyYAML: Para leer el archivo de configuración en YAML.
- requests-oauthlib: Para facilitar la conexión con la API de Twitter.
