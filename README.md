# Desarrollo de un Sistema de Alerta Temprana para el Monitoreo del Desplazamiento de Terreno en el Volcán Irazú Basado en Tecnología LoRa
# Integrantes
- Gerardo Araya Fallas
- Carlos Elizondo Alfaro
- Walter Serrano Concepción
- Fabián Chacón Solano

# Diagramas de nivel

<img title="a title" alt="Alt text" src="images/readme_images/primer_nivel.png">

- **Sensor de desplazamiento:** Mide el desplazamiento de la masa de tierra.
- **Módulo Lora:** Transmite los datos del sensor a una estación base.
- **Estación base:** Recibe datos del módulo LoRa y los envía a un servidor a través de internet.
- **Servidor en la nube:** Recibe y almacena datos, realiza análisis y genera alertas.
- **Interfaz de usuario:** Permite la visualización de datos y alertas en tiempo real.  

<br/>

<img title="a title" alt="Alt text" src="images/readme_images/segundo_nivel.png">


# LoRa APRS Tracker/Station
Este Firmware es para ser usado en Tarjetas ESP32 con módulos LoRa y GPS para funcionar en APRS.

## Pruebas iniciales del módulo de rastreo LoRa APRS

El módulo de rastreo a utilizar en este proyecto es el __T-Beam-AXP2101-V1.2__

Modelo de Prueba

<img src="images/modelocopia.png" alt="drawing" width="400"/>


Pruebas Iniciales del Tracker

<img src="images/OLEDtracker.png" alt="drawing" width="300"/>


Prueba de Rastreo en Mapa <a href="https://aprs.fi/#!lat=9.9354&lng=-84.1032" target="_blank">APRS</a>

<img src="images/Mapa.png" alt="drawing" width="200"/>



__(NOTA: Para usar las capacidades TX/RX de este rastreador debe tener también un LoRa iGate cerca de usted. Esto porque el rastreador se comunica con un iGate para enviar y recibir los datos para ser vistos en la red APRS. Idealmente, ese iGate se debe de encontrar en línea vista.)__


____________________________________________________

# WIKI (English / Español)

### FAQ: GPS, Bluetooth, Winlink, BME280 and more --> <a href="https://github.com/richonguzman/LoRa_APRS_Tracker/wiki/00.-FAQ-(frequently-asked-questions)" target="_blank">here</a>

### Supported Boards and buying links --> <a href="https://github.com/richonguzman/LoRa_APRS_Tracker/wiki/1000.-Supported-Boards-and-Buying-Links" target="_blank">here</a>

### 1. Installation Guide --> <a href="https://github.com/richonguzman/LoRa_APRS_Tracker/wiki/01.-Installation-Guide-%23-Guia-de-Instalacion" target="_blank">here</a>

### 2. Tracker Configuration and Explanation for each setting --> <a href="https://github.com/richonguzman/LoRa_APRS_Tracker/wiki/02.-Tracker-Configuration--%23--Configuracion-del-Tracker" target="_blank">here</a>

### 3. Upload Firmware and Filesystem --> <a href="https://github.com/richonguzman/LoRa_APRS_Tracker/wiki/03.-Upload-Firmware-and-Filesystem-%23-Subir-Firmware-y-sistema-de-archivos" target="_blank">here</a>

### 4. Tracker Menu Guide --> <a href="https://github.com/richonguzman/LoRa_APRS_Tracker/wiki/04.-Menu-Guide-%23-Guía-del-menú" target="_blank">here</a>




# Pasos de diseño:
- Definir los entregables.
- Definir los paquetes de trabajo (son las tareas internas de los entregables), lo cual incluye las plataformas a utilizar con el dispositivo y las personas asignadas para realizar cada tarea, si se le hace algún empaquetado al dispostivo, todo depende de cada entregable en el proyecto.
- Estimar el trabajo en cuanto a tiempo y costo (el scope de cada tarea), estimación del workpackage, de esta manera es posible calcular presupuestos.
- Agenda del trabajo (cuándo nos va a dar el entregable).

En un gráfico de Gantt
- Se agrega un objetivo, ejemplo: diseñar la interfase de despliegue de datos del módulo.
- Workpackage => Crear la interface en watson.
- Se asigna una persona con un tiempo de entrega.
- Asegurar los recursos para el proyecto (elementos adicionales de los que ya nos han brindado), porta baterías, baterías, componentes electrónicos, etc. Esto se consigna a una lista y se le llama BOM (Bill of materials), también puede haber recurso humano, por ejemplo solicitar a algún externo colaboración,no necesariamente el recurso humano va en el BOM, usualmente en esta parte van los componentes que se requieren para construir o terminar de ensamblar el producto, esta tabla también puede incluir los costos. Importante poner el part number de los componentes en la tabla.
- Posteriormente se incorpora el presupuesto a la agenda, esto significa que es necesario tener listos los componentes antes de que comience una tarea que requiera el recurso.
- Identificar los indicadores de rendimiento o funcionamiento, por ejemplo cuántas medidas obtuvimos de la comunicación de los dispositivos.
- Identificar factores críticos del proyecto, por ejemplo componentes que no se encuentran en stock y es necesario tenerlos en cuenta para el seguimiento del proyecto.
- Los indicadores funcionan para el test bench, es el banco de pruebas a ejecutar para comprobar que este va acorde a los entregables del proyecto. El diseño va enfocado a las pruebas que se realizan con el test bench, en la documentación se debe plasmar la información de los casos críticos y en qué no se puede utilizar. "Este dispositivo solo funciona para....". Si se logra todas las comunicaciones o no, hay que diseñar el dispositivo en el rango según los casos identificados.
- Añadir un 30% de costos al presupuesto inicial permite tener un margen para imprevistos.
- Entregable 12 de Agosto, diagramas de primer, segundo y tercer nivel y comenzar a montar el esqueleto del diseño del proyecto.


____________________________________________________
## Este código esta basado en el trabajo de:
- https://github.com/aprs434/lora.tracker : Serge - ON4AA on base91 byte-saving/encoding
- https://github.com/lora-aprs/LoRa_APRS_Tracker : Peter - OE5BPA LoRa Tracker
- https://github.com/Mane76/LoRa_APRS_Tracker : Manfred - DC2MH (Mane76) mods for multiple Callsigns and processor speed
- https://github.com/dl9sau/TTGO-T-Beam-LoRa-APRS : Thomas - DL9SAU for the Kiss <> TNC2 lib
- https://github.com/richonguzman/LoRa_APRS_Tracker Richonguzman - LoRa_APRS_Tracker
- https://github.com/richonguzman/LoRa_APRS_iGate Richonguzman - LoRa_APRS_iGate
____________________________________________________
