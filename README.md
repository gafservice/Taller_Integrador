# Desarrollo de un Sistema de Alerta Temprana para el Monitoreo del Desplazamiento de Terreno en el Volcán Irazú Basado en Tecnología LoRa
# Integrantes
- Gerardo Araya Fallas
- Carlos Elizondo Alfaro
- Walter Serrano Concepción
- Fabián Chacón Solano

# Introducción

## Objetivo principal


- Desarrollo de un Sistema de Alerta Temprana para el
Monitoreo del Desplazamiento de Terreno en el Volcán
Irazú Basado en Tecnología LoRa

### Descripción del problema

- El proyecto tiene como meta realizar un sistema de monitoreo en el volcán Irazú, esto con el fin de analizar el movimiento de tierras que existe en la zona, específicamente en la ubicación de las antenas, lugar donde previamente se han producido deslizamientos de relevancia y afectaron las comunicaciones en su momento por las antenas que cayeron.

- De esta manera se agrega un sistema de monitoreo que mide la distancia en metros desde el origen hasta la grieta por analizar, cuando se detecta un desplazamiento relevante fuera de los últimos datos obtenidos se lanza una alarma.

### Fotografías del área

#### Grietas presentes en el área

<img title="a title" alt="Alt text" src="images/readme_images/desplazamiento1.jpeg">

#### Desplazamientos de tierra ocurridos en el pasado 

<img title="a title" alt="Alt text" src="images/readme_images/desplazamiento2.jpeg">




# Horas de distribución para la ejecución del proyecto

| **Fase del Proyecto**      | **Tarea**                                  | **Horas Estimadas (Redondeadas)** |
|----------------------------|--------------------------------------------|-----------------------------------|
| **Planificación**          | Definir requisitos y especificaciones del sistema | 13                                |
|                            | Identificar los componentes necesarios     | 5                                 |
|                            | Establecer cronograma y asignar recursos   | 8                                 |
| **Diseño**                 | Esquema de hardware (circuito electrónico) | 20                                |
|                            | Diseño de firmware (software para dispositivos) | 27                            |
|                            | Diseño de software de aplicación           | 33                                |
|                            | Diseño de interfaz gráfica                 | 13                                |
| **Desarrollo**             | Prototipado de dispositivos                | 27                                |
|                            | Programación del firmware                  | 40                                |
|                            | Desarrollo de la aplicación                | 50                                |
|                            | Pruebas de integración                     | 20                                |
| **Pruebas y Validación**   | Pruebas de alcance                         | 13                                |
|                            | Pruebas de consumo de energía              | 10                                |
|                            | Pruebas de seguridad                       | 10                                |
|                            | Pruebas de usabilidad                      | 8                                 |
| **Documentación**          | Documentación técnica                      | 13                                |
|                            | Guías de usuario                           | 11                                |
| **Implementación**         | Despliegue del sistema                     | 13                                |
|                            | Capacitación de usuarios                   | 7                                 |
| **Soporte y Mantenimiento**| Soporte técnico                            | 13                                |
|                            | Actualizaciones de firmware y software     | 20                                |
|                            | Mantenimiento del sistema                  | 13                                |
| **Total de Horas Estimadas**|                                           | **405**                           |


# Diagramas de nivel

<img title="a title" alt="Alt text" src="images/readme_images/primer_nivel.png">

- **Sensor de desplazamiento:** Mide el desplazamiento de la masa de tierra.
- **Módulo Lora:** Transmite los datos del sensor a una estación base.
- **Estación base:** Recibe datos del módulo LoRa y los envía a un servidor a través de internet.
- **Servidor en la nube:** Recibe y almacena datos, realiza análisis y genera alertas.
- **Interfaz de usuario:** Permite la visualización de datos y alertas en tiempo real.  

<br/>

<img title="a title" alt="Alt text" src="images/readme_images/segundo_nivel.png">

## Diagramas de tercer Nivel

<img src="images/readme_images/tallint_dn03.png" alt="drawing" width="600"/>
<img src="images/readme_images/tallint_dn04.png" alt="drawing" width="600"/>
<img src="images/readme_images/tallint_dn05.png" alt="drawing" width="600"/>
<img src="images/readme_images/tallint_dn06.png" alt="drawing" width="600"/>
<img src="images/readme_images/talling_dn07.png" alt="drawing" width="600"/>

## Diagrama de cuarto nivel

<img src="images/readme_images/4toNivel.png" alt="drawing" width="600"/>

# LoRa APRS Tracker/Station
Este Firmware es para ser usado en Tarjetas ESP32 con módulos LoRa y GPS para funcionar en APRS.

## Pruebas iniciales del módulo de rastreo LoRa APRS

El módulo de rastreo a utilizar en este proyecto es el __T-Beam-AXP2101-V1.2__

Modelo de Prueba

<img src="images/modelocopia.png" alt="drawing" width="600"/>


Pruebas Iniciales del Tracker

<img src="images/OLEDtracker.png" alt="drawing" width="300"/>


Prueba de Rastreo en Mapa <a href="https://aprs.fi/#!lat=9.9354&lng=-84.1032" target="_blank">APRS</a>

<img src="images/Mapa.png" alt="drawing" width="200"/>




# Implementación del sistema

<img src="images/readme_images/implementacion.png" alt="drawing"/>

# Gráficas y reportes

### Packets transmitidos por hora
<img src="images/readme_images/graph_1.jpg" alt="drawing"/>

### Packets enviados mediante RF al sitio APRS
<img src="images/readme_images/graph_2.jpg" alt="drawing"/>

### Packets escuchados/recibidos por el tracker
<img src="images/readme_images/graph_3.jpg" alt="drawing"/>


## Aparición en sitio APRS

<img src="images/readme_images/aprs_site.png" alt="drawing"/>

## Demostración de interfaz gráfica para obtención de datos


<img src="images/readme_images/reporte_power_bi.png" alt="drawing"/>

# Interfaz programada y línea de comandos

<img src="images/readme_images/python.jpg" alt="drawing"/>

<img src="images/readme_images/command_line.jpg" alt="drawing"/>