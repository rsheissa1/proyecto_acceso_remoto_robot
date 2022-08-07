# Three Broketers Team
# Basado en el trabajo de © 2022 Digi International Inc.
# https://www.digi.com/resources/documentation/Digidocs/90001541/reference/r_example_subscribe_mqtt.htm

# RemoteArm_v_1_0
# 14/07/2022
# - Se reenvía el mensaje recibido por el subscriptor hacia el puerto serie.
# - Traducción de los comentarios de la fuente del código.

# Bibliotecas
import paho.mqtt.client as mqtt
import serial, time



# Inicialización de puertos seriales (Requiere programación adicional para manejar identificadores de trama)
pserie0 = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=0.3) # Configuración del puerto serie 0
#pserie1 = serial.Serial('/dev/ttyUSB1', baudrate=9600, timeout=0.3) # Configuración del puerto serie 1
#pserie2 = serial.Serial('/dev/ttyUSB2', baudrate=9600, timeout=0.3) # Configuración del puerto serie 2


def on_connect(client, userdata, flags, rc):  # Función callback para cuando el cliente conecta con el broker
    print("Connected with result code {0}".format(str(rc)))  # Imprime el resultado del intento de conexión
    client.subscribe("/uv/lab1/robot1")  # Se suscribe al tópico: “/uv/lab1/robot1”, y recibe cualquier mensaje publicado en él.

def on_message(client, userdata, msg):  # Función callback para cuando el broker publica un mensaje y es recibido desde el servidor.
    print("Message received-> " + msg.topic + " " + str(msg.payload))  # Imprime el mensaje recibido
    """
    pserie0.flushInput()   # Limpia buffer de entrada
    pserie0.flushOutput()  # Limpia buffer de salida
    pserie0.write(msg.payload)   # Manda trama por el puerto serie 0
    """
client = mqtt.Client("RemoteArmBuggy1")  # Crea una instancia cliente con el ID:  “RemoteArmBuggy1”
client.on_connect = on_connect  # Define la función "callback" para una conexión exitosa.
client.on_message = on_message  # Define la función "callback" para recepción de mensaje.
client.connect("broker.hivemq.com", 1883, 60) # Subscripción al broker
client.loop_forever() 