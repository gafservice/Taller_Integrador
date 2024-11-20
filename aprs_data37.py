import aprslib
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

# Configuración del servidor APRS
server = "rotate.aprs.net"
port = 14580
callsign = "GAF"  # Nombre del iGate
passcode = "29347"
tracker_callsign = "GAFw-11"

# Mensaje recibido desde el servidor APRS
mensaje_recibido = "GAFw-11>APRS,qAO,TI2HAS-11:!/IKWT95yK_,(H.../...g...t076r...p...P...h82b....."

def decodificar_mensaje(mensaje):
    try:
        # Decodificación usando aprslib
        parsed_message = aprslib.parse(mensaje)

        # Mostrar el mensaje crudo para diagnóstico
        print("Mensaje crudo decodificado:", parsed_message)

        # Extraer información clave
        lat = parsed_message.get("latitude", "No disponible")
        lon = parsed_message.get("longitude", "No disponible")
        spd = parsed_message.get("speed", "No disponible")
        crs = parsed_message.get("course", "No disponible")
        sat = parsed_message.get("satellite", "No disponible")
        dis = parsed_message.get("distance", "No disponible")
        comentario = parsed_message.get("comment", "No disponible")
        from_call = parsed_message.get("from", "No disponible")
        to = parsed_message.get("to", "No disponible")
        path = parsed_message.get("path", "No disponible")
        via = parsed_message.get("via", "No disponible")

        # Obtener temperatura y humedad desde el subdiccionario "weather"
        weather = parsed_message.get("weather", {})
        temp = weather.get("temperature", "No disponible")
        hum = weather.get("humidity", "No disponible")

        # Redondear la temperatura a dos decimales si es un número
        if isinstance(temp, (int, float)):
            temp = round(temp, 2)

        # Información adicional opcional
        informacion = {
            "latitud": lat,
            "longitud": lon,
            "velocidad": spd,
            "curso": crs,
            "satélites": sat,
            "distancia": dis,
            "temperatura": temp,
            "humedad": hum,
            "comentario": comentario,
            "from": from_call,
            "to": to,
            "path": path,
            "via": via,
            "raw": parsed_message
        }
        return informacion
    except Exception as e:
        return {"error": str(e)}

# Función para obtener la hora local (ajustada a GMT-6)
def obtener_hora_local():
    utc_now = datetime.utcnow()
    local_time = utc_now - timedelta(hours=6)
    return local_time.strftime("%H:%M:%S")  # Solo hora

# Función para obtener la fecha local (ajustada a GMT-6)
def obtener_fecha_local():
    utc_now = datetime.utcnow()
    local_time = utc_now - timedelta(hours=6)
    return local_time.strftime("%Y-%m-%d")  # Solo fecha

# Función para actualizar los datos
def actualizar_datos():
    # Decodificar el mensaje recibido
    resultado = decodificar_mensaje(mensaje_recibido)
    
    # Mostrar resultados en la terminal
    if "error" in resultado:
        print(f"Error al decodificar el mensaje: {resultado['error']}")
    else:
        print("\nDatos decodificados:")
        print("Fecha Local:", obtener_fecha_local())  # Imprimir fecha local
        print("Hora Local:", obtener_hora_local())   # Imprimir hora local
        for clave, valor in resultado.items():
            if clave != "raw":
                print(f"{clave.capitalize()}: {valor}")
        print("Mensaje completo:", resultado["raw"])

    # Actualizar la interfaz gráfica
    mostrar_grafico(resultado)

    # Llamar a la función nuevamente después de 15 segundos (15000 ms)
    ventana.after(15000, actualizar_datos)

# Crear la interfaz gráfica
def mostrar_grafico(resultado):
    ventana = tk.Tk()
    ventana.title("Datos Decodificados APRS")

    # Crear un marco para los datos
    frame = ttk.Frame(ventana, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

    # Título
    ttk.Label(frame, text="Datos Decodificados APRS", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

    if "error" in resultado:
        # Mostrar error en la ventana
        ttk.Label(frame, text=f"Error: {resultado['error']}", foreground="red").grid(row=1, column=0, columnspan=2, pady=5)
    else:
        # Mostrar la fecha y hora local
        fila = 1
        ttk.Label(frame, text=f"Fecha Local: {obtener_fecha_local()}", font=("Arial", 12)).grid(row=fila, column=0, columnspan=2, pady=5)
        fila += 1
        ttk.Label(frame, text=f"Hora Local: {obtener_hora_local()}", font=("Arial", 12)).grid(row=fila, column=0, columnspan=2, pady=5)
        fila += 1
        # Mostrar cada variable con su nombre y valor
        for clave, valor in resultado.items():
            if clave != "raw":
                ttk.Label(frame, text=f"{clave.capitalize()}: ", font=("Arial", 12, "bold")).grid(row=fila, column=0, sticky=tk.W, pady=5, padx=10)
                ttk.Label(frame, text=f"{valor}", font=("Arial", 12)).grid(row=fila, column=1, sticky=tk.W, pady=5, padx=10)
                fila += 1

    # Botón para cerrar la ventana
    ttk.Button(frame, text="Cerrar", command=ventana.destroy).grid(row=fila, column=0, columnspan=2, pady=10)

    # Ejecutar la interfaz gráfica
    ventana.mainloop()

# Iniciar la actualización de los datos
actualizar_datos()

