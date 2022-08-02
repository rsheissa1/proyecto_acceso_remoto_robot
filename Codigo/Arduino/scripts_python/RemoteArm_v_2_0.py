# Three Broketers Team
# Basado en el trabajo de © 2022 Digi International Inc.
# https://www.digi.com/resources/documentation/Digidocs/90001541/reference/r_example_subscribe_mqtt.htm

# RemoteArm_v_2_0 14/07/2022
# - Se agrega código para manejo de varias instrucciones y temporizado entre tramas
# RemoteArm_v_1_0 12/07/2022
# - Se reenvía el mensaje recibido por el subscriptor hacia el puerto serie.
# - Traducción de los comentarios de la fuente del código.

# Bibliotecas
import paho.mqtt.client as mqtt
import serial, time

broker = "broker.hivemq.com"

# Inicialización de puertos seriales (Requiere programación adicional para manejar identificadores de trama)
pserie0 = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=0.3) # Configuración del puerto serie 0
#pserie1 = serial.Serial('/dev/ttyUSB1', baudrate=9600, timeout=0.3) # Configuración del puerto serie 1
#pserie2 = serial.Serial('/dev/ttyUSB2', baudrate=9600, timeout=0.3) # Configuración del puerto serie 2
print("Conectando a /uv/lab1/test1 . . .")

def on_connect(client, userdata, flags, rc):  # Función callback para cuando el cliente conecta con el broker
    print("¡Conexión exitosa!".format(str(rc)))  # Imprime el resultado del intento de conexión
    client.subscribe("/uv/lab1/test1")  # Se suscribe al tópico: “/uv/lab1/robot1”, y recibe cualquier mensaje publicado en él.

def on_message(client, userdata, msg):  # Función callback para cuando el broker publica un mensaje y es recibido desde el servidor.
    mens = str(msg.payload)
    trama = mens[2:len(mens)-1]  # elimina los identificadores binarios
    print("Mensaje recibido de " + msg.topic + " : " + trama)  # Imprime el mensaje recibido
    x = trama.split(',')   
    
    n=0
    for i in range(int(len(x)/2)):
       # print(i)
        print('\n' + 'Instrucción: ' + str(i+1))
        print('Ejecutado: ' + str(x[n]))
        ret=int(x[n+1])
        print('Esperando: ' + str(ret))
        print('\n')
        
        pserie0.flushInput()   # Limpia buffer de entrada
        pserie0.flushOutput()  # Limpia buffer de salida
        pserie0.write(x[n].encode())   # Manda trama por el puerto serie 0
        time.sleep(ret)
        n += 2
    print('terminado')   
    
client = mqtt.Client("RemoteArmBuggy1")  # Crea una instancia cliente con el ID:  “RemoteArmBuggy1”
client.on_connect = on_connect  # Define la función "callback" para una conexión exitosa.
client.on_message = on_message  # Define la función "callback" para recepción de mensaje.
client.connect(broker, 1883, 60) # Subscripción al broker
client.loop_forever() 