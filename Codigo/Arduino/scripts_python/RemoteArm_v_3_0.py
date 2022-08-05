# Three Broketers Team
# Basado en el trabajo de © 2022 Digi International Inc.
# https://www.digi.com/resources/documentation/Digidocs/90001541/reference/r_example_subscribe_mqtt.htm

# RemoteArm_v_3_0 04/08/2022
# - Cambia la forma de empleo de las funciones de "paho" para un cierre correcto de las llamadas a procesos
# - Se logra hacer conecciòn entre clientes y subscriptores dentro de un red local mediante sus IP respectivas
# RemoteArm_v_2_1 21/07/2022
# - Se corrige error al enviar trama no se mandaba el retorno de carro
# RemoteArm_v_2_0 14/07/2022
# - Se agrega código para manejo de varias instrucciones y temporizado entre tramas
# RemoteArm_v_1_0 12/07/2022
# - Se reenvía el mensaje recibido por el subscriptor hacia el puerto serie.
# - Traducción de los comentarios de la fuente del código.

# Bibliotecas

import paho.mqtt.client as mqtt # Import the client
import time, serial

# Inicialización de puertos seriales (Requiere programación adicional para manejar identificadores de trama)
pserie0 = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=0.3) # Configuración del puerto serie 0
#pserie1 = serial.Serial('/dev/ttyUSB1', baudrate=9600, timeout=0.3) # Configuración del puerto serie 1
#pserie2 = serial.Serial('/dev/ttyUSB2', baudrate=9600, timeout=0.3) # Configuración del puerto serie 2

def on_message(client, userdata, message):
    print("Recieved message: ", str(message.payload.decode("utf-8"))) # Imprime en terminal el mensaje recibido

    mens = str(message.payload) # Convierte a cadena de texto
    trama = mens[2:len(mens)-1]  # elimina los identificadores binarios
    print("Mensaje recibido de " + message.topic + " : " + trama)  # Imprime el dato ya procesado para envìo a motores yel cliente del que proviene
    x = trama.split(',')

    n=0
    for i in range(int(len(x)/2)):
       # print(i)
        print('\n' + 'Instrucción: ' + str(i+1)) # Imprime el nùmero de instucciòn
        print('Ejecutado: ' + str(x[n]))  # Imprime el contenido de la instrucciòn
        ret=int(x[n+1])  # Obtienen el siguiente dato a la instrucciòn (retardo)
        print('Esperando: ' + str(ret)) # Imprime el valor del retardo
        print('\n')

        pserie0.flushInput()   # Limpia buffer de entrada
        pserie0.flushOutput()  # Limpia buffer de salida
        pserie0.write(x[n].encode())   # Manda trama por el puerto serie 0
        pserie0.write(b'\x13')
        time.sleep(ret)
        n += 2
    print('terminado') # Fin del proceso de instrucciones



while True:
    mqttBroker = "192.168.3.5"


    client = mqtt.Client("rob2") # Crea una nueva instancia
    client.connect(mqttBroker, 1883, keepalive=25) # Conexta al broker (IP del cliente)

    client.loop_start() # Inicia el ciclo

    client.subscribe("/uv/lab1/rob2")
    client.on_message = on_message # llamada a la funciòn callback

    time.sleep(10) # Espera 10 segundos
    client.loop_stop() # Detienen el ciclo
