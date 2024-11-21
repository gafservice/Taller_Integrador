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

## Demostración de interfaz gráfica para obtención de datos


<img src="images/readme_images/reporte_power_bi.png" alt="drawing"/>


<img src="images/readme_images/Igate:_config_01.png" alt="drawing"/>


<img src="images/readme_images/Igate_config_02.png" alt="drawing"/>


<img src="images/readme_images/Igate_config_03.png" alt="drawing"/>

